
import os, fnmatch
from pathlib import Path

path = Path("c:/Users/leeuw582/OneDrive - KPN BV/Desktop/P3c/Working with Files/files")

def ends_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)   
            
def starts_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)   
            
            
# ends_with(path, '.txt')
starts_with(path, '02_file')
