import os
import shutil
import sys

WORKING_DIR = 'saitenGiri2021'

def is_working_directory():
    return os.path.basename(os.getcwd()) == WORKING_DIR  
    
def test_is_working_directory(): 
    assert is_working_directory() == True 
    
def is_contain(path, dir):
    files = os.listdir(path)
    dirs = [f for f in files if os.path.isdir(os.path.join(path, f))]
    print(dirs)
    return dir in dirs

def copy_dir(dir, path):
    shutil.copytree(dir, path)
    
def test_is_contain():
    assert is_contain('./', 'fixture') == True

def copy_sample(path):
    if not is_working_directory():
        print("The current directory is not "+ WORKING_DIR+".\n")
        sys.exit()
    else:
        if is_contain('./','setting') == True:
           print("setting directory is exist!\n")
           sys.exit()
        else:
            shutil.copytree(path,'setting') 

#print(is_contain('./', 'fixture'))
copy_sample('./fixture/setting')