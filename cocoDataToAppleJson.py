
import json
from pathlib import Path
import os
import shutil

birdFileNameArray = []

#写真に含まれる一羽の鳥のannotationデータを、Appleの指定するDictionary形式で生成する関数。
def makeOneAnnotationDictionary(height,width,x,y):
    annotationDictionary = {'label':"bird",  #今回は鳥だけ認識
                            'coordinates':{'height': height, 
                                           'width': width,
                                           'x': x, 
                                           'y': y
                                          }
                           } 
    return annotationDictionary

#一枚の写真に含まれる複数もしくは単数の鳥のannotationデータを、
#写真の名前とともにAppleの指定するDictionary形式で生成する関数。
def makeOneImageDictionary(birdsLocationsArray,name):
    annotationDictionariesArray = [] #これがannotationsキーに対する値となる。
    for item in birdsLocationsArray:
        dictionary = makeOneAnnotationDictionary(item[3],item[2],item[0],item[1]) #height,width,x,yの順にする
        annotationDictionariesArray.append(dictionary)
    imageDictionary = {'image': str(name),  
                       'annotations': annotationDictionariesArray
                      } 
    return imageDictionary

#鳥の写真内での位置と、写真の名前をセットにした配列を生成する関数。
def makeBirdsLocationsArray(annotations) :
    birdPictureArray = []
    for i in range(len(annotations)):
      #鳥は、"category_id": 16 っぽい。(instances_val2017.jsonから見つけた。)
      if annotations[i]["category_id"] == 16 :
        birdPictureArray.append([annotations[i]["bbox"],annotations[i]["image_id"]])
    return birdPictureArray

#appleの指定するJson形式を生成する関数。
def makeAppleAnnotationsFormat(birdLocationsArray):
    dictionary = {}
    #鳥の写真内での位置と、写真の名前をセットにした配列を
    #写真の名前をkey、鳥の写真内での位置をvalueとした辞書の形に落とし込む
    for i in range(len(birdLocationsArray)):  
        dictionary.setdefault(birdLocationsArray[i][1], []).append(birdLocationsArray[i][0])
    array = []
    for key in dictionary:
        #ここでfile名(key)について、番号の前に0をたくさんつけて12桁の名前にしないといけない。
        name = str(key).zfill(12) + ".jpg"
        makeBirdFileNameArray(name)
        array.append(makeOneImageDictionary(dictionary[key],name))
    return array

#Appleの指定するjson形式のファイルを書き出す関数。
def createAnnotationJsonFile(readFilePath,writePath):
    # ファイルを開く
    jsonFile = open(readFilePath, 'r')
    # JSONとして読み込む
    jsonObj  = json.load(jsonFile)
    annotations = jsonObj["annotations"] 
    birdLocationsArray = makeBirdsLocationsArray(annotations)
    data = makeAppleAnnotationsFormat(birdLocationsArray)
    # 辞書オブジェクトをJSONファイルへ出力
    with open(str(writePath) + '/annotations.json', mode='wt', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)  

#鳥を含んだ写真の名前の配列を作る関数。
def makeBirdFileNameArray(name):
    birdFileNameArray.append(name)

#COCOに含まれる鳥の写真のみを、ValDataやTraningDataのフォルダにコピーする関数。
def getBirdPictures(cocoPicturePath,savePath):
    for name in birdFileNameArray:
        shutil.copyfile(str(cocoPicturePath) + name,str(savePath) + "/" + name)
    birdFileNameArray.clear()
    

cocoFilePath = input('Enter coco directory path: ')
path = Path(cocoFilePath)   # cocoディレクトリのパス
# cocoディレクトリの一つ上の階層に移動してValDataのディレクトリを作成
path /= '../ValData/'     
#ValDataというディレクトリを作成。
os.makedirs(path,exist_ok=True)

#ValDataディレクトリの中に、annotationファイルを入れる。
cocoValAnnotaionsPath = cocoFilePath + "annotations/instances_val2017.json"
createAnnotationJsonFile(cocoValAnnotaionsPath,path)
#ValDataディレクトリの中に、cocoに含まれる鳥の写真のみをコピーする。
cocoValPicturePath = cocoFilePath + "images/val2017/"
getBirdPictures(cocoValPicturePath,path)

# ValDataディレクトリの一つ上の階層に移動してTraningDataのディレクトリを作成
path /= '../TraningData/'   
#TraningDataというディレクトリを作成。
os.makedirs(path,exist_ok=True)

#TrainingDataディレクトリの中に、annotationファイルを入れる。
cocoTraningAnnotaionsPath = cocoFilePath + "annotations/instances_train2017.json"
createAnnotationJsonFile(cocoTraningAnnotaionsPath,path)
#TrainingDataディレクトリの中に、cocoに含まれる鳥の写真のみをコピーする。
cocoValPicturePath = cocoFilePath + "images/train2017/"
getBirdPictures(cocoValPicturePath,path)