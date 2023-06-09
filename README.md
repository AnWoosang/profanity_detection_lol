# [profanity_detection_lol] - 리그오브레전드 채팅 욕설 검출을 위한 이미지 처리모델
(Image Processing Model for League of Legends Chat Profanity Detection)<br><br><br>

## Background
 변칙적 혐오표현을 포함한 비속어 검출 모델을 개발하기 위해 해당 프로젝트를 진행하였습니다. <br>
 대표적으로 변칙적 혐오표현이 많이 등장하는 Realworld의 케이스를 찾고자 리그오브레전드라는 게임을 선정하였습니다. <br>
 해당 모델은 () repository에 있는 자연어처리 모델과 함께 사용하였으며, 저희가 진행한 부분에 대해서만 업로드를 했다는 점 참고 해주시면 감사하겠습니다.<br>
<br><br><br> 

## Purpose of this Model
 게임 내에서 특수문자등을 활용한 변칙적 비속어 검출을 하기 위해 리그 오브 레전드의 채팅을 포함한 인게임 화면 데이터 속에 채팅창과 문장을 검출하고 이를 텍스트화 한다.
<br><br><br> 
 
## 사용 모델
#### YOLOv5 - ultralytics/yolov5 [https://github.com/ultralytics/yolov5.git]
1) Chatting Window Detecting Model - (약 500개의 League of Legend 인게임 화면캡쳐 데이터를 통해 훈련된 모델)
2) Chat Line Detecting Model - (약 1200개의 League of Legend 인게임 화면캡쳐 데이터를 통해 훈련된 모델)


#### clovaai/deep-text-recognition-benchmark [https://github.com/clovaai/deep-text-recognition-benchmark.git]
1) Text Recognition Model (제작한 한글 단어 데이터를 python3의 trdg로 조합해 만든 약 530만개의 문장 데이터를 통해 훈련된 모델)
  - None-ResNet-BiLSTM-Attn 옵션 모델
<br>
*훈련하고자 한다면 원래 Repository를 통해서 훈련 방법을 참고하세요
<br><br>

## Requirements

<br>

- install Requirements

```shell
pip3 install -r requirements.txt
```
(안될 경우 아래의 Command 사용)

- Yolo <br>

```shell
pip3 install torch opencv-python pandas tqdm torchvision matplotlib seaborn numpy pillow pyyaml
```
<br><br>
- Deep-text-recognition-benchmark<br>

```shell
pip3 install lmdb natsort
```


<br><br><br>
## Download Model
- Detection 모델은 이미 포함되어 있음
- Text-Recognition 모델 (https://drive.google.com/file/d/13GO1S61qnms_73YnIFOaBe1ZTHRuT_d-/view)
- 위의 모델 파일을 다운받아 clova/saved_models에 넣어준다.

## Process
1)  - 롤 인게임 화면 데이터에서 채팅창을 검출할 수 있는 yolov5모델 (saved_models/chat_window_detector.pt)을 통해서 채팅창 crop 이미지 아웃풋을 저장
    - 인식의 정확도를 고려하여 resize.py를 통해 이미지를 확대 후 저장
2)  - 채팅창 crop image를 다시 채팅 line을 검출할 수 있는 yolov5모델 (saved_models/line_detector.pt)를 통해서 채팅 line crop 이미지 아웃풋을 저장
    - 채팅 line crop 이미지를 resize.py를 통해 이미지를 확대 후 저장
3)  - 채팅 line crop 이미지를 deep-text-recognition-benchmark 모델에 통과시켜 이미지에 있는 텍스트를 검출 
<br><br><br>
## 실행 코드
* yolo/image 디렉터리 내부에 채팅창을 포함하고 있는 롤 인게임 화면 이미지 데이터들을 넣는다.<br><br>

1) Chatting Window Detection (yolo 디렉터리 내에서)<br>
```shell
python3 detect.py --weights ./saved_models/chat_window_detector.pt --hide-labels --name chat_win --source image --classes 0 --save-crop --project ./chatwin --name result
```
2) Resize<br>
- 실행하기 전 이전과정에서 crop이미지가 어디에 저장 되어있는지 확인하세요.<>
```shell
python3 resize.py --source chatwin/result/crops/chat_win --output_dir resized_chatwin
```

3) Chat Line Detection (yolo 디렉터리 내에서)<br>
```shell
python3 detect.py --weights ./saved_models/line_detector.pt --hide-labels --name line_detect --source ./resized_chatwin --classes 2 --save-crop --project ./chat_line --name result
```
4) Resize<br>
- 실행하기 전 이전과정에서 crop이미지가 어디에 저장 되어있는지 확인하세요.<br>
```shell
python3 resize.py --source chat_line/result/crops/line --output_dir resized_chat_line
```
- resized_chat_line을 clova 디렉터리 하위로 이동<br>
```shell
mv resized_chat_line ../clova
```
<br><br>

5) Text Recognition (clova 디렉터리 내에서)<br>
```shell
python3 demo.py --image_folder resized_chat_line --saved_model ./saved_models/text_recognition.pth --Transformation None --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn
```
<br><br><br>
## Output Example
* Original Image<br>
![data148](https://github.com/AnWoosang/profanity_detection_lol/assets/79970034/9eabdfb1-3002-4da3-a5b7-649978e19d52)
<br><br>
1) Chatting Window Crop Image<br>
![data148_double](https://github.com/AnWoosang/profanity_detection_lol/assets/79970034/22b54231-d574-4ddb-9ab4-ddcc75eba0d5)
<br><br>
2) Chatting Line Crop Image<br>
![data148_double6_double](https://github.com/AnWoosang/profanity_detection_lol/assets/79970034/9c241871-6620-437d-be0a-f3793899c6a7)
<br><br>
3) Output<br>
![data148_╤МтХгтФд╤ЛтЦС╨Р_2](https://github.com/AnWoosang/profanity_detection_lol/assets/79970034/9b4d2e3f-98b3-4002-bc02-13a3b29dab66)
<br>
- 모든 이미지에 존재하는 채팅 line이 완벽하게 텍스트화 되지는 않지만 정확하게 나온 결과를 반영하여 작성했다. (위의 결과 예시는 Chatting Window에 있는 Line 중 일부만을 보여준 결과)
<br><br><br>

## 특수문자를 활용한 변칙적 비속어에 대한 텍스트 검출

<br>
1) 원본 이미지<br>

![data7](https://github.com/AnWoosang/profanity_detection_lol/assets/79970034/0294cc24-973b-4f2c-b218-8f42aea1d5b5)
<br><br>
3) 검출 텍스트<br>
 
![image](https://github.com/AnWoosang/profanity_detection_lol/assets/79970034/5a81a75c-34ca-4549-8081-0d9ca27e561d)







