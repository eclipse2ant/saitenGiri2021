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

  # 戻るボタン
	backB = Button(
  button_frame, text='一つ前に戻る', command=back_one, width=20, height=4).pack()

  # 入力完了
	finB = Button(
  button_frame, text='入力完了\n(保存して戻る)', command=trim_fin, width=20, height=4).pack()
	topB = Button(
        button_frame, text='topに戻る\n(保存はされません)', command=toTop, width=20, height=4).pack()

	canvas1.bind("<ButtonPress-1>", start_point_get)
	canvas1.bind("<Button1-Motion>", rect_drawing)
	canvas1.bind("<ButtonRelease-1>", release_action)
	Giri_cutter.mainloop()

# 透過画像の作成 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# https://stackoverflow.com/questions/54637795/how-to-make-a-tkinter-canvas-rectangle-transparent/54645103
# 透過画像を削除するときは、imagesの配列から消す。
images = []  # to hold the newly created image


def back_one():
    global qCnt
    if qCnt == 0:
        return
    qCnt = qCnt - 1
    # タグに基づいて画像を削除
    if qCnt == 0:
        canvas1.delete("nameBox", "nameText", "rectTmp")
        images.pop(-1)
    else:
        canvas1.delete("qBox" + str(qCnt), "qText" + str(qCnt), "rectTmp")
        images.pop(-1)
    # csvの最終行を削除
    readFile = open("setting/ini.csv")
    lines = readFile.readlines()
    readFile.close()
    w = open("setting/ini.csv", 'w')
    w.writelines([item for item in lines[:-1]])
    w.close()


