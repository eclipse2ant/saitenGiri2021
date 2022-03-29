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


class Windows:
    def __init__(self,attr):
        self.fifwid = 500
        self.val = 0.4
        self.fifhet = 400
        
        self.window_h = 700
        self.window_w = int(self.window_h * 1.7)
        self.fig_area_w = int(self.window_h * 1)
        
        self.attr = attr
        self.set_tk(self.attr)
        
    def set_tk(self, attr):
        self.tk = Tk()
        self.tk.title(attr['title'])
        self.tk.geometry(attr['geometry'])
        self.tk.configure(bg=attr['bg'])


    def do(self):
        self.init()
        self.tk.mainloop()
  
    def init(self):
        Pass
        

  
    # 画像パスの取得
    # https://msteacher.hatenablog.jp/entry/2020/06/27/170529
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


