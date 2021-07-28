import json
from pathlib import Path
import cv2
import os

cocoFilePath = input('Enter coco directory path: ')
path = Path(cocoFilePath)   # cocoディレクトリのパス
# 移動
path /= '../ValData/annotations.json'     
json_open = open(path, 'r')
json_data = json.load(json_open)

path = Path(cocoFilePath)   # cocoディレクトリのパス
# cocoディレクトリの一つ上の階層に移動してVisualizedValDataのディレクトリを作成
path /= '../VisualizedValData/'     
os.makedirs(path,exist_ok=True)

path = Path(cocoFilePath)   # cocoディレクトリのパス
# cocoディレクトリの一つ上の階層に移動
path /= '../'   

for data in json_data:
    print("reading >>> " + data["image"])
    img = cv2.imread(str(path) + "/ValData/"+ data["image"])
    for annotation in data["annotations"]:
        x = int(annotation["coordinates"]["x"])
        y = int(annotation["coordinates"]["y"])
        w = int(annotation["coordinates"]["width"])
        h = int(annotation["coordinates"]["height"])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
        cv2.imwrite(str(path) + "/VisualizedValData/" + data["image"], img)

