import os
import sys

WORKING_DIR = 'saitenGiri2021'

def test_chehking_working_directory(): 
    assert os.path.basename(os.getcwd()) == WORKING_DIR
    