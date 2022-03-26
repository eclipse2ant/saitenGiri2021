import os
import csv
import glob


def initDir():
	os.makedirs("./setting/input", exist_ok=True)
	os.makedirs("./setting/output", exist_ok=True)
	f = open('setting/ini.csv', 'w')  # 既存でないファイル名を作成してください
	writer = csv.writer(f, lineterminator='\n')  # 行末は改行
	writer.writerow(["tag", "start_x", "start_y", "end_x", "end_y"])
	f.close()

def get_sorted_files(dir_path):
	all_sorted = sorted(glob.glob(dir_path))
	fig_sorted = [s for s in all_sorted if s.endswith(
    ('jpg', "jpeg", "png", "PNG", "JPEG", "JPG", "gif"))]
	return fig_sorted

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
  
def exxt_filter(files, extlist):
  return ([name for name in files if name.split(".")[-1] in extlist])
