import os
from datetime import datetime
from pathlib import Path

def get_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%d %b %Y')


def get_file_attrs(fld):
    with os.scandir(fld) as dir:
        for f in dir:
            if f.is_file():
                info = f.stat()
                print(f"File Name: {f.name}")
                print(f"  Size: {info.st_size} bytes")
                print(f"  Created: {get_date(info.st_ctime)}")
                print(f"  Last Modified: {get_date(info.st_mtime)}")
                print(f"  Last Accessed: {get_date(info.st_atime)}")
                print()
                
path = Path("c:/Users/leeuw582/OneDrive - KPN BV/Desktop/P3c/Working with Files/files")
get_file_attrs(path)