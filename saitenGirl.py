from ast import Pass
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
from Windows import Windows 

class SaitenGirl(Windows):
  
    def init(self):
        self.top_frame = Frame(self.tk, bg="white")		
        self.top_frame.pack()
        self.fig_frame = Frame(self.top_frame, width=self.fifwid, height=self.fifhet)
        self.fig_frame.grid(column=0, row=0)
        self.f_data_list = [{'name': "nfo" , 'command': self.info, 'text': "はじめに",},
            {'name': "setting_ok", 'command': self.setting_ck, 'text': "初期設定をする"},
            {'name': "input_ok", 'command': self.input_ck, 'text': "どこを斬るか決める"},
            {'name': "trimck", 'command': self.trimck, 'text': "全員の解答用紙を斬る"}
            ]

        try:
            self.topimg = Image.open(self.resource_path("top.png"))
            self.topimg = self.topimg.resize(
                (int(self.topimg.width * self.val), int(self.topimg.height * self.val)), 0)
            self.topfig = ImageTk.PhotoImage(self.topimg, master=self.tk)
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
 #           giri.GirActivate()
            window_h = 700
            window_w = int(window_h * 1.7)
            fig_area_w = int(window_h * 1)

            attr = {'title': "解答用紙を斬る", 'geometry': str(window_w) + "x" + 
                str(window_h), 'bg': "grey90"}
            giri.Giri(attr).do()


    def trimck(self):
        ret = messagebox.askyesno(
    'すべての解答用紙を斬っちゃいます。', '全員の解答用紙を、斬ります。\n以下の注意を読んで、よければ始めてください。\n\n ①受験者が100人以上いると、5分ほど時間がかかります。進捗は、一緒に起動したウィンドウに表示されています。\n②inputに保存された画像は、削除されません。\n③現在のoutputは全て消えます。')
        if ret == True:
            trim.allTrim()
        else:
            pass


  
    # 画像パスの取得
    # https://msteacher.hatenablog.jp/entry/2020/06/27/170529
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    attr = {'title': "採点ギリギリ", 'geometry': "800x400", 'bg': "white"}
    SaitenGirl(attr).do()
    