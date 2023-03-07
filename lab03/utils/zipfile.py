import os
from zipfile import ZipFile

def unarchive(file_path: str):
    with ZipFile(file_path, 'r') as zip:
        base_path, _ = os.path.split(file_path)

        zip.printdir()

        print('Extracting all the files now...')
        zip.extractall(base_path)
        print('Done!')