import os
from pathlib import Path

path = Path("c:/Users/leeuw582/OneDrive - KPN BV/Desktop/P3c/Working with Files/files")

def list_dir(fld):
    for fn in os.listdir(fld):
        print(fn)       
        
        
list_dir(path)