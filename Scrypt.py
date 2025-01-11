from os import listdir
from os.path import isfile, join, isdir
import os
import shutil

def is_folder_empty(folder_path):
    return len(listdir(folder_path)) == 0

file_path = r"C:\Users\ivko0\Downloads"
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

for file in files:
    filename, filetype = os.path.splitext(file)
    filetype = filetype[1:]  # Remove the dot from the file extension

    # manage Folders
    folder_name = join(file_path, filetype + '_folder')

    if not isdir(folder_name):
        os.mkdir(folder_name)

    # manage Files
    src_file = join(file_path, file)
    dest_file = join(folder_name, file)

    if not os.path.exists(dest_file):
        shutil.move(src_file, dest_file)
    else:
        new_dest_file = join(folder_name, f"{filename}_i.{filetype}")
        shutil.move(src_file, new_dest_file)

# Remove empty folders
for folder in listdir(file_path):
    folder_path = join(file_path, folder)
    if isdir(folder_path) and is_folder_empty(folder_path):
        os.rmdir(folder_path)