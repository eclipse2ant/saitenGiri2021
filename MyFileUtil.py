from lzma import FILTER_DELTA
import os
import csv
import glob
import pathlib


def initDir():
    os.makedirs("./setting/input", exist_ok=True)
    os.makedirs("./setting/output", exist_ok=True)
    f = open('setting/ini.csv', 'w')  # 既存でないファイル名を作成してください
    writer = csv.writer(f, lineterminator='\n')  # 行末は改行
    writer.writerow(["tag", "start_x", "start_y", "end_x", "end_y"])
    f.close()

def get_sorted_filterd_files(dir_path):
    return get_filtered_files(get_all_sorted_files(dir_path))
    
def get_all_sorted_files(dir_path):
    return sorted(glob.glob(dir_path))

def  get_filtered_files(list):
    return [s for s in list if s.endswith(
        ('jpg', "jpeg", "png", "PNG", "JPEG", "JPG", "gif"))]

def readCSV(datafile):
  # もしcsvが無ければ、全部止める
    if os.path.isfile(datafile) == False:
        return 0
    else:
        with open(datafile) as f: 
            reader = csv.reader(f)
            data = [row for row in reader]
            data.pop(0)
            return data
  
def ext_filter(files, extlist):
  return ([name for name in files if name.split(".")[-1] in extlist])

def addpath(path, file):
    return (path + "/" + file)

def if_mkdir(dir):
    if os.path.isdir(dir) == False:
        os.makedirs(dir)


def folder_walker(folder_path, recursive=False, file_ext=".*"):
    """
    指定されたフォルダのファイル一覧を取得する。
    引数を指定することで再帰的にも、非再帰的にも取得可能。

    Parameters
    ----------
    folder_path : str
        対象のフォルダパス
    recursive : bool
        再帰的に取得するか否か。既定値はTrueで再帰的に取得する。
    file_ext : str
        読み込むファイルの拡張子を指定。例：".jpg"のようにピリオドが必要。既定値は".*"で指定なし
    """

    p = pathlib.Path(folder_path)

    if recursive:
        return list(p.glob("**/*" + file_ext))  # **/*で再帰的にファイルを取得
    else:
        return list(p.glob("*" + file_ext))  # 再帰的にファイル取得しない

