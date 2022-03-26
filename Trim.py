import csv
import os
import sys
import shutil
from PIL import Image, ImageTk, ImageDraw, ImageFont  # 外部ライブラリ

import MyFileUtil as fu

datafile = "./setting/trimData.csv"
#output_dir = "./setting/output"
# トリミング前の画像の格納先
ORIGINAL_FILE_DIR = "./setting/input"
# トリミング後の画像の格納先
TRIMMED_FILE_DIR = "./setting/output"

extlist =  ['jpg', "jpeg", "png", "PNG", "JPEG", "JPG", "gif"]


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
	#files = os.listdir(ORIGINAL_FILE_DIR)
	#print(files)
  # 特定の拡張子のファイルだけを採用。実際に加工するファイルの拡張子に合わせる
	files = fu.exxt_filter(os.listdir(ORIGINAL_FILE_DIR), extlist)

	try:
		for val in files:
  		# オリジナル画像へのパス
			path = ORIGINAL_FILE_DIR + "/" + val
			# トリミングされたimageオブジェクトを取得
			im = Image.open(path)
			print(val + "を斬ります" )
			for pos in data:
      	# 出力フォルダのパス
				title , left , top , right , bottom = pos
				outputDir = TRIMMED_FILE_DIR + "/" + title
        # もしトリミング後の画像の格納先が存在しなければ作る
				if os.path.isdir(outputDir) == False:
					os.makedirs(outputDir)
					im_trimmed = im.crop((int(left), int(top), int(right), int(bottom)))
          # qualityは95より大きい値は推奨されていないらしい
					im_trimmed.save(outputDir + "/" + val, quality=95)
					print("___"+ title + "を斬り取りました。" )
					print("********************************")
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


allTrim()



      