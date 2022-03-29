from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont  # 外部ライブラリ

import os
import csv
import shutil
import MyFileUtil as fu
from Windows import Windows

class Saiten(Windows):
    def init(self):
        # macにおける、.DS_storeを無視してカウントする。
        maxNinzu = len([f for f in next(os.walk("./setting/input/"))[2] if not f.startswith('.')])

        # outputの中のフォルダを取得
        path = "./setting/output/"
        files = os.listdir(path)
        files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
        files_dir.sort()
        lb = Listbox(self.tk, selectmode='single', height=20, width=20)
        clcounter = 0
        for i in files_dir:
            if not i == "name":
                misaiten = len([f for f in next(os.walk("./setting/output/" + i))[2] if not f.startswith('.')])
                lb.insert(END, i)
                if misaiten == maxNinzu:
                    lb.itemconfig(clcounter, {'bg': 'white'})
                elif misaiten == 0:
                    lb.itemconfig(clcounter,  {'bg': 'gray'})
                else:
                    lb.itemconfig(clcounter,  {'bg': 'pale green'})
                clcounter = clcounter + 1

        lb.grid(row=0, column=0)
        # Scrollbar
        scrollbar = Scrollbar(
            self.tk,
            orient=VERTICAL,
            command=lb.yview)
        lb['yscrollcommand'] = scrollbar.set
        scrollbar.grid(row=0, column=1,  sticky=(N, S, W))

        button_frame = Frame(self.tk)
        button_frame.grid(row=0, column=1, sticky=W +
                      E + N + S, padx=30, pady=30)

        siroKaisetsu = Label(button_frame, text="未採点", bg="white").pack(
            side=TOP, fill=X)
        midoriKaisetsu = Label(button_frame, text="採点中", bg="pale green").pack(
            side=TOP, fill=X)
        grayKaisetsu = Label(button_frame, text="採点終了", bg="gray").pack(
            side=TOP, fill=X)

        button1 = Button(
            button_frame, text='採点する', width=15, height=3,
            command=lambda: self.show_selection()).pack(expand=True)

        totopB = Button(
            button_frame, text='Topに戻る', width=15, height=3,
            command=self.backTop).pack()

