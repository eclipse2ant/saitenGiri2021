import os
import sys

def up(path):
    return os.path.dirname(path)

parent_dir = up(up(up(os.path.abspath(__file__))))
sys.path.append(parent_dir)

from Saiten import Saiten

def test_maxNinzu():
    attr = {'title': "採点する問題を選ぶ", 'geometry': "500x500", 
                'bg': "grey90"}
    saiten = Saiten(attr)
    t1 = saiten.maxNinzu()
    t2  = 10
    assert t1 == t2
    
def test_get_files():
    attr = {'title': "採点する問題を選ぶ", 'geometry': "500x500", 
                'bg': "grey90"}

    saiten = Saiten(attr)
    print(saiten.get_files(saiten.OUTPUT_PATH))
    t1 = saiten.get_files(saiten.OUTPUT_PATH)
    t2 = ['name', 'Q_0001', 'Q_0002', 'Q_0003', 'Q_0004', 'Q_0005',
          'Q_0006', 'Q_0007', 'Q_0008', 'Q_0009', 'Q_0010', 'Q_0011']
    assert t1 == t2

def test_get_dirs():
    attr = {'title': "採点する問題を選ぶ", 'geometry': "500x500", 
                'bg': "grey90"}

    saiten = Saiten(attr)
    print(saiten.get_dirs(saiten.OUTPUT_PATH))
    t1 = saiten.get_dirs(saiten.OUTPUT_PATH)
    t2 = ['Q_0001', 'Q_0002', 'Q_0003', 'Q_0004', 'Q_0005', 'Q_0006',
          'Q_0007', 'Q_0008', 'Q_0009', 'Q_0010', 'Q_0011', 'name']
    assert t1 == t2



#test_get_files()
#test_get_dirs()
