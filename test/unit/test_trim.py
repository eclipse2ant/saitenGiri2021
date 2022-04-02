import sys
sys.path.append('../')

from Trim import *
import MyFileUtil as fu

def test_readcsv():
    datafile = "./setting/trimData.csv"
    t1 = fu.readCSV(datafile)
    t2 = [['name', '337', '37', '507', '81'], ['Q_0001', '62', '126', '185', '264'], 
        ['Q_0002', '55', '271', '190', '318'], ['Q_0003', '54', '326', '189', '375'],
        ['Q_0004', '61', '378', '190', '432'], ['Q_0005', '63', '441', '187', '481'],
        ['Q_0006', '58', '486', '189', '541']]
    assert t1 == t2

def test_extfilter(): 
    ORIGINAL_FILE_DIR = "./setting/input"
    extlist =  ['jpg', "jpeg", "png", "PNG", "JPEG", "JPG", "gif"]
    t1 = fu.ext_filter(os.listdir(ORIGINAL_FILE_DIR), extlist)
    t2 = ['答案01.jpg', '答案02.jpg', '答案03.jpg', '答案04.jpg', '答案05.jpg', 
       '答案06.jpg', '答案07.jpg', '答案08.jpg', '答案09.jpg', '答案10.jpg']
    assert t1 == t2
 
  
