import csv
import os
import sys
import shutil
import glob
from turtle import pos
from PIL import Image, ImageTk, ImageDraw, ImageFont  # 外部ライブラリ

import MyFileUtil as fu

datafile = "./setting/trimData.csv"
#output_dir = "./setting/output"
# トリミング前の画像の格納先
ORIGINAL_FILE_DIR = "./setting/input"
# トリミング後の画像の格納先
TRIMMED_FILE_DIR = "./setting/output"

extlist =  ['jpg', "jpeg", "png", "PNG", "JPEG", "JPG", "gif"]

def make_trim_data(file, dir, data):
    return {'file': file, 'dir': dir, 'data': data}

def do_trim(image, output_dir, pos, file): 
    title , left , top , right , bottom = pos
    # 出力フォルダのパス
    # もしトリミング後の画像の格納先が存在しなければ作る
    fu.if_mkdir(fu.addpath(output_dir, title))
    im_trimmed = image.crop((int(left), int(top), int(right), int(bottom)))
    # qualityは95より大きい値は推奨されていないらしい
    im_trimmed.save(fu.addpath(fu.addpath(output_dir, title), file), quality=95)
    print(fu.addpath(fu.addpath(output_dir, title), file))
    print("___"+ title + "を斬り取りました。" )
    print("********************************")
    

def trim(t_data):
  
    # トリミングされたimageオブジェクトを取得
    image = Image.open(fu.addpath(t_data['dir'],t_data['file']))
    print(t_data['file'] + "を斬ります" )
    
    for pos in t_data['data']:
        do_trim(image, TRIMMED_FILE_DIR, pos, t_data['file'])

def allTrim():
    data = fu.readCSV(datafile)
    try:
        shutil.rmtree(TRIMMED_FILE_DIR)
    except OSError as err:
        pass
    
    if data == 0:
        print('終了', 'どうやって斬ればいいかわかりません。\nまずはどこを斬るかを決めてください。')
    #	messagebox.showinfo('終了', 'どうやって斬ればいいかわかりません。\nまずはどこを斬るかを決めてください。')
        return 0

  # 画像ファイル名を取得	
  # 特定の拡張子のファイルだけを採用。実際に加工するファイルの拡張子に合わせる
    files = fu.ext_filter(os.listdir(ORIGINAL_FILE_DIR), extlist)
    #print(files)
    try:
        for file in files:
            trim(make_trim_data(file,  ORIGINAL_FILE_DIR, data))
    except:
            print(
        'エラー', 'エラーが検出されました。中断します。\n\n' + str(sys.stderr))

#			messagebox.showinfo(
#        'エラー', 'エラーが検出されました。中断します。\n\n' + str(sys.stderr))
            try:
                shutil.rmtree("./setting/output")
            except OSError as err:
                pass
            return 0

    # nameフォルダの中身をリサイズ
    # maxheight以上のときは、小さくする。
    maxheight = 50
    files = glob.glob("./setting/output/name/*")
    img = Image.open(files[0])
    namew, nameh = img.size
    if nameh > maxheight:
        rr = nameh / maxheight
        for f in files:
            img = Image.open(f)
            img = img.resize((int(namew / rr), int(nameh/rr)))
            img.save(f)


#allTrim()



      