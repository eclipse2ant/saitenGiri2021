import sys

# 一個上の階層をpathに追加
sys.path.append('../')

from Saiten import Saiten



def test_readcsv():
    attr = {'title': "採点する問題を選ぶ", 'geometry': "500x500", 
                'bg': "grey90"}
    saiten = Saiten(attr)
    t1 = saiten.maxNinzu()
    t2  = 10
    assert t1 == t2
    