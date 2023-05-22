# [profanity_detection_lol] - 리그오브레전드 채팅 욕설 검출을 위한 이미지 처리모델(Image Processing Model for League of Legends Chat Profanity Detection)

## Purpose of this Model
 게임 내에서 특수문자등을 활용한 변칙적 비속어 검출을 하기 위해 리그 오브 레전드의 채팅을 포함한 인게임 화면 데이터 속에 채팅창과 문장을 검출하고 이를 텍스트화 한다.
 
## 사용한 모델
ultralytics/yolov5
clovaai/deept-text-recognition-benchmark

## Process
1)  - 롤 인게임 화면 데이터에서 채팅창을 검출할 수 있는 yolov5모델 (saved_models/chat_window_detector.pt)을 통해서 채팅창 crop 이미지 아웃풋을 저장
    - 인식의 정확도를 고려하여 resize.py를 통해 이미지를 확대 후 저장
2)  - 채팅창 crop image를 다시 채팅 line을 검출할 수 있는 yolov5모델 (saved_models/line_detector.pt)를 통해서 채팅 line crop 이미지 아웃풋을 저장
    - 채팅 line crop 이미지를 resize.py를 통해 이미지를 확대 후 저장
3)  - 채팅 line crop 이미지를 deep-text-recognition-benchmark 모델에 통과시켜 이미지에 있는 텍스트를 검출

python3 detect.py --weights chat_window_detector.pt --hide-labels --name chat_test --source image --classes 0 --save-crop

## Output
* Original Image
![data148](https://github.com/AnWoosang/profanity_detection_lol/assets/79970034/54117403-e8e2-4c8c-8c79-f570367f7fec)

1) Chatting Window Crop Image
![data148_double](https://github.com/AnWoosang/profanity_detection_lol/assets/79970034/16ab3510-1cf8-4998-92f4-f067bcc281a4)

2) Chatting Line Crop Image

3) Output


- 모든 이미지에 존재하는 채팅 line이 완벽하게 텍스트화 되지는 않으나


