import os
from datetime import datetime
from pathlib import Path


def traverse(fld):
    for fldpath, dirs, fls in os.walk(fld):
        print(f"Folder: {fldpath} ")
        for fn in fls:
            print(f"\t{fn}")


path = Path("c:/Users/leeuw582/OneDrive - KPN BV/Desktop/P3c/Working with Files/files")
traverse(path)
