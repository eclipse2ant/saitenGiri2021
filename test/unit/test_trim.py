import os
import sys


def up(path):
    return os.path.dirname(path)
parent_dir = up(up(up(os.path.abspath(__file__))))
sys.path.append(parent_dir)


from Trim import *
import mFileUtil as fu

def test_readcsv():
    datafile = "./setting/trimData.csv"
    print(fu.readCSV(datafile))
    t1 = fu.readCSV(datafile)
    t2 = [['name', '331', '27', '507', '79'], ['Q_0001', '56', '128', '187', '265'],
          ['Q_0002', '57', '266', '192', '321'], ['Q_0003', '51', '318', '193', '375'],
          ['Q_0004', '56', '371', '193', '432'], ['Q_0005', '57', '426', '186', '483'],
          ['Q_0006', '50', '480', '191', '543'], ['Q_0007', '59', '542', '190', '597'],
          ['Q_0008', '50', '594', '193', '654'], ['Q_0009', '49', '647', '194', '706'],
          ['Q_0010', '56', '706', '187', '753'], ['Q_0011', '221', '128', '347', '321']]
   
    assert t1 == t2

def test_extfilter(): 
    ORIGINAL_FILE_DIR = "./setting/input"
    extlist =  ['jpg', "jpeg", "png", "PNG", "JPEG", "JPG", "gif"]
    t1 = fu.ext_filter(os.listdir(ORIGINAL_FILE_DIR), extlist)
    t2 = ['答案01.jpg', '答案02.jpg', '答案03.jpg', '答案04.jpg', '答案05.jpg', 
       '答案06.jpg', '答案07.jpg', '答案08.jpg', '答案09.jpg', '答案10.jpg']
    assert t1 == t2
 
#print(fu.readCSV("./setting/trimData.csv"))  
