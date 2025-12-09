import os
dirname = os.path.dirname(__file__)
print(dirname)

entries = os.listdir(dirname)
for entry in entries:
    if os.path.isdir(os.path.join(dirname, entry)):
        print(f"{entry} is a directory")
    else:
        print(f"{entry} is a file")

filename = os.path.join(dirname, 'cleanupFolder/temp.txt')

with open(filename, 'r') as file:
    content = file.read()
    print(content)