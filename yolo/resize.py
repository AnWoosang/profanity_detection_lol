import os
import shutil
import glob
import argparse
from PIL import Image


parser = argparse.ArgumentParser()
parser.add_argument('--source', default='', help='images source directory')
parser.add_argument('--output_dir', default='', help='images output directory')
opt = parser.parse_args()

files = glob.glob(opt.source+'/*.jpg')
new_path = opt.output_dir
if new_path in os.listdir(os.getcwd()): 
    shutil.rmtree(new_path)
    # os.remove(new_path)
os.mkdir(new_path)

for f in files:
    img = Image.open(f)
    # img_resize = img.resize((int(img.width * 2), int(img.height * 2)))
    img_resize = img.resize((1000, int(round(img.height/img.width, 10)*1000)))

    title, ext = os.path.splitext(f)
    print(title[title.index('/'):].split('/')[-1])
    
    img_resize.save(new_path+'/'+title[title.index('/'):].split('/')[-1] + '_resize' + ext)
    # 50 / 50 * 500 -> 500

