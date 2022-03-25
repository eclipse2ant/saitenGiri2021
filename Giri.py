from tkinter import *
from tkinter import messagebox

import os
import csv
import MyFileUtil as fu

def GirActivate():
	global RESIZE_RETIO
	global img_resized
	global canvas1
	global img_tk
	global Giri_cutter
	global qCnt
 
	def toTop():
		global qCnt
		ret = messagebox.askyesno(
    '保存しません', '作業中のデータは保存されません。\n画面を移動しますか？')
		if ret == True:
			qCnt = 0
			Giri_cutter.destroy()
		else:
			pass

	# 表示する画像の取得
	files = fu.get_sorted_files(os.getcwd() + "/setting/input/*")
	print(files)
  
  
	# ini.csvは、起動のたびに初期化する。
	f = open('setting/ini.csv', 'w')  # 既存でないファイル名を作成してください
	writer = csv.writer(f, lineterminator='\n')  # 行末は改行
	writer.writerow(["tag", "start_x", "start_y", "end_x", "end_y"])
	f.close()

	img = Image.open(files[0])

	# ini.csvは、起動のたびに初期化する。
	f = open('setting/ini.csv', 'w')  # 既存でないファイル名を作成してください
	writer = csv.writer(f, lineterminator='\n')  # 行末は改行
	writer.writerow(["tag", "start_x", "start_y", "end_x", "end_y"])
	f.close()

	img = Image.open(files[0])


