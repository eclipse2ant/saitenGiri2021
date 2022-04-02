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
    
test_get_files()
