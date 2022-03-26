from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont  # 外部ライブラリ

import os
import csv
import shutil
import MyFileUtil as fu

window_h = 700
window_w = int(window_h * 1.7)
fig_area_w = int(window_h * 1)
#global qCnt
qCnt = 0

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

	f_data_list = [{'name': "back_one" , 'command': back_one, 'text': "一つ前に戻る",},
			{'name': "trim_fin", 'command': trim_fin, 'text': "入力完了\n(保存して戻る)"},
			{'name': "toTop", 'command': toTop, 'text': "topに戻る\n(保存はされません)"}
    	]
	exBool = True
	botWid = 20

	for f_data in f_data_list:
		Button(
			button_frame, text=f_data["text"], command=f_data["command"], width=botWid, height=2, highlightthickness=0).pack(expand=exBool)
  
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


def trim_fin():
	global Giri_cutter
	ret = messagebox.askyesno('終了します', '斬り方を決定し、ホームに戻っても良いですか？')
	if ret == True:
		cur = os.getcwd()
		beforePath = cur + "/setting/ini.csv"
		afterPath = cur + "/setting/trimData.csv"
		shutil.move(beforePath, afterPath)
		Giri_cutter.destroy()

# ドラッグ開始した時のイベント - - - - - - - - - - - - - - - - - - - - - - - - - -
def start_point_get(event):
  global start_x, start_y  # グローバル変数に書き込みを行なうため宣言

  canvas1.delete("rectTmp")  # すでに"rectTmp"タグの図形があれば削除

  # canvas1上に四角形を描画（rectangleは矩形の意味）
  canvas1.create_rectangle(event.x,
                            event.y,
                            event.x + 1,
                            event.y + 1,
                            outline="red",
                            tag="rectTmp")
    # グローバル変数に座標を格納
  start_x, start_y = event.x, event.y


# ドラッグ中のイベント - - - - - - - - - - - - - - - - - - - - - - - - - -


def rect_drawing(event):

  # ドラッグ中のマウスポインタが領域外に出た時の処理
  if event.x < 0:
    end_x = 0
  else:
    end_x = min(img_resized.width, event.x)
  if event.y < 0:
    end_y = 0
  else:
    end_y = min(img_resized.height, event.y)

  # "rectTmp"タグの画像を再描画
  canvas1.coords("rectTmp", start_x, start_y, end_x, end_y)



def release_action(event):
	global qCnt

	if qCnt == 0:
		pos = canvas1.bbox("rectTmp")

  	# canvas1上に四角形を描画（rectangleは矩形の意味）
		create_rectangle_alpha(pos[0], pos[1], pos[2], pos[3],
                               fill="green",
                               alpha=0.3,
                               tag="nameBox"
                               )

		canvas1.create_text(
            (pos[0] + pos[2]) / 2, (pos[1] + pos[3]) / 2,
            text="name",
            tag="nameText"
        )

  	# "rectTmp"タグの画像の座標を元の縮尺に戻して取得
		start_x, start_y, end_x, end_y = [
            round(n * RESIZE_RETIO) for n in canvas1.coords("rectTmp")
    	]
		with open('setting/ini.csv', 'a') as f:
			writer = csv.writer(f, lineterminator='\n')  # 行末は改行
			writer.writerow(["name", start_x, start_y, end_x, end_y])

	else:
		pos = canvas1.bbox("rectTmp")
    # canvas1上に四角形を描画（rectangleは矩形の意味）
		create_rectangle_alpha(pos[0], pos[1], pos[2], pos[3],
                               fill="red",
                               alpha=0.3,
                               tag="qBox" + str(qCnt)
                               )
		canvas1.create_text(
            (pos[0] + pos[2]) / 2, (pos[1] + pos[3]) / 2,
            text="Q_" + str(qCnt),
            tag="qText" + str(qCnt)
        )

    # "rectTmp"タグの画像の座標を元の縮尺に戻して取得
		start_x, start_y, end_x, end_y = [
            round(n * RESIZE_RETIO) for n in canvas1.coords("rectTmp")
        ]
		with open('setting/ini.csv', 'a') as f:
			writer = csv.writer(f, lineterminator='\n')  # 行末は改行
			writer.writerow(["Q_" + str(qCnt).zfill(4),
                            start_x, start_y, end_x, end_y])

	qCnt = qCnt + 1



def create_rectangle_alpha(x1, y1, x2, y2, **kwargs):
  if 'alpha' in kwargs:
    alpha = int(kwargs.pop('alpha') * 255)
    fill = kwargs.pop('fill')
    fill = Giri_cutter.winfo_rgb(fill) + (alpha,)
    image = Image.new('RGBA', (x2-x1, y2-y1), fill)
    images.append(ImageTk.PhotoImage(image, master=Giri_cutter))
    canvas1.create_image(x1, y1, image=images[-1], anchor='nw')
    canvas1.create_rectangle(x1, y1, x2, y2, **kwargs)
