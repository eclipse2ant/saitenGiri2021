from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont  # 外部ライブラリ

import os
import csv
import MyFileUtil as fu

window_h = 700
window_w = int(window_h * 1.7)
fig_area_w = int(window_h * 1)

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

	# 画面サイズに合わせて画像をリサイズする
	# 画像サイズが縦か横かに合わせて、RESIZE_RETIOを決める。
	w, h = img.size
	if w >= h:
		if w <= fig_area_w:
			RESIZE_RETIO = 1
		else:
			RESIZE_RETIO = h / window_h
	else:
		if h <= window_h:
			RESIZE_RETIO = 1
		else:
			RESIZE_RETIO = h / window_h

	# 画像リサイズ
	img_resized = img.resize(size=(int(img.width / RESIZE_RETIO),
                                int(img.height / RESIZE_RETIO)),
                          resample=Image.BILINEAR)

	Giri_cutter = Tk()
	Giri_cutter.geometry(str(window_w) + "x" + str(window_h))
	Giri_cutter.title("解答用紙を斬る")

	cutting_frame = Frame(Giri_cutter)
	cutting_frame.pack()
	canvas_frame = Frame(cutting_frame)
	canvas_frame.grid(column=0, row=0)
	button_frame = Frame(cutting_frame)
	button_frame.grid(column=1, row=0)
 
  # tkinterで表示できるように画像変換
	img_tk = ImageTk.PhotoImage(img_resized, master=Giri_cutter)

  # Canvasウィジェットの描画
	canvas1 = Canvas(canvas_frame,
                             bg="black",
                             width=img_resized.width,
                             height=img_resized.height,
                             highlightthickness=0)
  # Canvasウィジェットに取得した画像を描画
	canvas1.create_image(0, 0, image=img_tk, anchor=NW)

  # Canvasウィジェットを配置し、各種イベントを設定
	canvas1.pack()


