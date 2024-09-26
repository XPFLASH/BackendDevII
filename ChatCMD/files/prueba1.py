import os

path = './files'

obj = os.scandir(path)

for entry in obj:
    if entry.is_dir() or entry.is_file():
        print(entry.name)