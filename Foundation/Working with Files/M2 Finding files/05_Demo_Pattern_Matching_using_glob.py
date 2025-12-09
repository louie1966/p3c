import os, fnmatch
from pathlib import Path

path = "c:/Users/leeuw582/OneDrive - KPN BV/Desktop/P3c/Working with Files/files"


def glob_match(fld, search):
    p = Path(fld)
    for n in p.glob(search):
        print(n)


glob_match(path + "/subfolder", "*_file.*")
