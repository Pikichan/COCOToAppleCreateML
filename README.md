### **COCOの写真を、AppleのCreateMLの物体認識で扱うデータセットの形に変換する🤗**  

・`cocoDataToAppleJson.py`をそのまま使うと、  
　COCOの写真群から鳥の映っている写真だけを抜き出して  
　鳥に関するannotationを作成するようになっている。

・`showRectangles.py`は、`cocoDataToAppleJson.py`を実行した後   
　生成されたデータがAppleのCreateMLの物体認識で扱うデータセットの形に  
 　正しく整形されているかどうかを確認するためのプログラム。
 
# 使い方
## 0. 事前準備
#### 1. COCOから画像データをダウンロードするためにスクリプトを入手する。   
こちらのスクリプトを使ってダウンロードするとスムーズ。👇  
https://gist.github.com/mkocabas/a6177fc00315403d31572e17700d7fd9  
#### 2. ダウンロードしたスクリプトを実行する。   
スクリプトを実行すると、`coco`というディレクトリが生成される。  
`coco`の中に`images`と`annotations`というディレクトリができている。

## 1. `cocoDataToAppleJson.py` を使う
1. `cocoDataToAppleJson.py` を好きな場所に置く。
2. `cocoDataToAppleJson.py`を実行すると、以下のような表示が出る。
```sh
Enter coco directory path: 
```
3. 上記の**0.事前準備**で出来た`coco`ディレクトリのパスを記入する。  
記入例👇
```sh
Enter coco directory path: /Users/Pikichan/coco/
```
4. `coco`ディレクトリの存在する階層と同じ階層に  
`ValData`ディレクトリと`TraningData`ディレクトリが生成される。  
これらのディレクトリは、AppleのCreateMLの物体認識で扱うデータセットの形に準拠しているので  
そのままCreateMLの画面にDrag & Drop できる！

## 2.`showRectangles.py`を使う(必須ではない)
1. `showRectangles.py` を好きな場所に置く。
2. `showRectangles.py`を実行すると、以下のような表示が出る。
```sh
Enter coco directory path: 
```
3. 上記の**0.事前準備**で出来た`coco`ディレクトリのパスを記入する。  
記入例👇
```sh
Enter coco directory path: /Users/Pikichan/coco/
```
4. `coco`ディレクトリや `ValData`ディレクトリの存在する階層と同じ階層に  
`VisualizedValData`ディレクトリができる。  
このディレクトリの中には、`ValData`ディレクトリと同じ画像が含まれているが、  
それぞれの画像内で認識したい物体が赤の枠で囲まれている画像となっている。  
例👇  
<img src="https://user-images.githubusercontent.com/59171751/127330468-166da165-29e2-4a45-87f4-7d6621f40465.jpg" width="320px">

`VisualizedValData`ディレクトリ内の画像を確認することで、  
「COCOの写真を、AppleのCreateMLの物体認識で扱うデータセットの形に正しく変換できている」ことが視覚的に確認できる。

# 鳥じゃない物体を認識するモデルのデータセットを作りたい時
`cocoDataToAppleJson.py`をちょこっと書き換えるだけで簡単にできる。
1. https://github.com/Pikichan/COCOToAppleCreateML/blob/3b61ab81fd07a726ce20db738449e483fcb326b8/cocoDataToAppleJson.py#L11  
の`"bird"`の部分を認識したい物体の名前に変更する。  
ここは個人の好きに名前をつけて良い。
2. https://github.com/Pikichan/COCOToAppleCreateML/blob/3b61ab81fd07a726ce20db738449e483fcb326b8/cocoDataToAppleJson.py#L37  
のidを、認識したい物体のidに変更する。  
どの物体にどのidが振られているかは以下のサイトが詳しい。  
https://tech.amikelive.com/node-718/what-object-categories-labels-are-in-coco-dataset/
