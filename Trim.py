import csv
import os
import sys
import shutil
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
		return 0

  # 画像ファイル名を取得
	#files = os.listdir(ORIGINAL_FILE_DIR)
	#print(files)
  # 特定の拡張子のファイルだけを採用。実際に加工するファイルの拡張子に合わせる
	print( fu.exxt_filter(os.listdir(ORIGINAL_FILE_DIR), extlist))

allTrim()



      