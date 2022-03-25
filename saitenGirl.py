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
			{'name': "input_ok", 'command': self.input_ck, 'text': "どこを斬るか決める"}
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
				self.initDir()
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
	