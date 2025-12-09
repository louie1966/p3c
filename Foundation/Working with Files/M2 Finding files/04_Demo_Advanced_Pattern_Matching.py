
import os, fnmatch
from pathlib import Path

path = Path("c:/Users/leeuw582/OneDrive - KPN BV/Desktop/P3c/Working with Files/files")

def match(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn,search):
            print(fn)   
            
match(path, '*_file.*')