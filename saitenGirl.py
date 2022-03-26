from asyncio.windows_events import NULL
from tkinter import *
from tkinter import messagebox

import os
import sys
import shutil
import pathlib
import imghdr
import openpyxl
import glob
import csv

from PIL import Image, ImageTk, ImageDraw, ImageFont

import MyFileUtil as fu
import Giri as giri
import Trim as trim

class SaitenGirl:
	def __init__(self):
		self.fifwid = 500
		self.val = 0.4
		self.fifhet = 400
		
		self.window_h = 700
		self.window_w = int(self.window_h * 1.7)
		self.fig_area_w = int(self.window_h * 1)
  
		self.root = Tk()
		self.root.title("採点ギリギリ")
		self.root.geometry("800x400")
		self.root.configure(bg='white')
		self.top_frame = Frame(self.root, bg="white")		
		self.top_frame.pack()
		self.fig_frame = Frame(self.top_frame, width=self.fifwid, height=self.fifhet)
		self.fig_frame.grid(column=0, row=0)
		self.f_data_list = [{'name': "nfo" , 'command': self.info, 'text': "はじめに",},
			{'name': "setting_ok", 'command': self.setting_ck, 'text': "初期設定をする"},
			{'name': "input_ok", 'command': self.input_ck, 'text': "どこを斬るか決める"},
   		{'name': "trimck", 'command': self.trimck, 'text': "全員の解答用紙を斬る"}
    	]
		

	def do(self):
		self.init()
		self.root.mainloop()
  
	def init(self):
		try:
			self.topimg = Image.open(self.resource_path("top.png"))
			self.topimg = self.topimg.resize(
				(int(self.topimg.width * self.val), int(self.topimg.height * self.val)), 0)
			self.topfig = ImageTk.PhotoImage(self.topimg, master=self.root)
			canvas_top = Canvas(
				bg="white", master=self.fig_frame, width=self.fifwid + 30, height=self.fifhet, highlightthickness=0)
			canvas_top.place(x=0, y=0)
			canvas_top.create_image(0, 0, image=self.topfig, anchor=NW)
			canvas_top.pack()
		except:
			pass

		button_frame = Frame(self.top_frame, bg="white", highlightthickness=0)
		button_frame.grid(column=1, row=0, sticky=W + E + N + S)
		
		exBool = True
		botWid = 20

		for f_data in self.f_data_list:
			Button(
			button_frame, text=f_data["text"], command=f_data["command"], width=botWid, height=2, highlightthickness=0).pack(expand=exBool)
			
	
	def info(self):
		messagebox.showinfo(
			"はじめに", "オンラインヘルプをご覧ください。\n https://phys-ken.github.io/saitenGiri2021/")

	def setting_ck(self):
		if not os.path.exists("./setting/"):
			ret = messagebox.askyesno(
       			'初回起動です', '採点のために、いくつかのフォルダーをこのファイルと同じ場所に作成します。\nよろしいですか？')
			if ret == True:
				fu.initDir()
				messagebox.showinfo(
        			'準備ができました。', '解答用紙を、setting/input の中に保存してください。jpeg または png に対応しています。')
			else:
				# メッセージボックス（情報）
				messagebox.showinfo('終了', 'フォルダは作成しません。')
		else:
			messagebox.showinfo(
       			'確認', '初期設定は完了しています。解答用紙を、setting/inputに入れてから、解答用紙分割をしてください。')

	def input_ck(self): 
		# 表示する画像の取得
		files = fu.get_sorted_files(os.getcwd() + "/setting/input/*")
		if not files:
    	# メッセージボックス（警告）
			messagebox.showerror(
            "エラー", "setting/inputの中に、解答用紙のデータが存在しません。画像を入れてから、また開いてね。")
		else:
			giri.GirActivate()


	def trimck(self):
		ret = messagebox.askyesno(
    'すべての解答用紙を斬っちゃいます。', '全員の解答用紙を、斬ります。\n以下の注意を読んで、よければ始めてください。\n\n ①受験者が100人以上いると、5分ほど時間がかかります。進捗は、一緒に起動したウィンドウに表示されています。\n②inputに保存された画像は、削除されません。\n③現在のoutputは全て消えます。')
		if ret == True:
			trim.allTrim()
		else:
			pass

	def addingpath(path, file):
		return (path + "/" + file)


	def allTrim():
  	# トリミング前の画像の格納先
		ORIGINAL_FILE_DIR = "./setting/input"
    # トリミング後の画像の格納先
		TRIMMED_FILE_DIR = "./setting/output"

		def readCSV():
    	# もしcsvが無ければ、全部止める
			if os.path.isfile("./setting/trimData.csv") == False:
				return 0
			else:
				with open('./setting/trimData.csv') as f:
					reader = csv.reader(f)
					data = [row for row in reader]
					data.pop(0)
					return data

		data = readCSV()

		try:
			shutil.rmtree("./setting/output")
		except OSError as err:
			pass

		if data == 0:
			messagebox.showinfo('終了', 'どうやって斬ればいいかわかりません。\nまずはどこを斬るかを決めてください。')
			return 0

    # 画像ファイル名を取得
		files = os.listdir(ORIGINAL_FILE_DIR)
    # 特定の拡張子のファイルだけを採用。実際に加工するファイルの拡張子に合わせる
		files = [name for name in files if name.split(
    	".")[-1] in ['jpg', "jpeg", "png", "PNG", "JPEG", "JPG", "gif"]]

		try:
			for val in files:
      	# オリジナル画像へのパス
				path = NULL
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
			messagebox.showinfo(
        'エラー', 'エラーが検出されました。中断します。\n\n' + str(sys.stderr))
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

		#output_name_sh()
		messagebox.showinfo('斬りました', '全員分の解答用紙を斬りました。')


  
	# 画像パスの取得
	# https://msteacher.hatenablog.jp/entry/2020/06/27/170529
	def resource_path(self, relative_path):
		if hasattr(sys, '_MEIPASS'):
			return os.path.join(sys._MEIPASS, relative_path)
		return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
	sg = SaitenGirl()
	sg.do()
	#sg.root.mainloop()
	