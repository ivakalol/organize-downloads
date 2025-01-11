from os import listdir
from os.path import isfile, join, isdir
import os
import shutil
import logging


    
def is_folder_empty(folder_path):
    return len(listdir(folder_path)) == 0

try: 
    file_path = r"C:\Users\Ivaka2\Downloads"
    files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

    for file in files:
        filename, filetype = os.path.splitext(file)
        filetype = filetype[1:].lower()  # Remove the dot from the file extension

        # manage Folders
        folder_name = join(file_path, filetype)

        if not isdir(folder_name):
            os.mkdir(folder_name)

        # manage Files
        src_file = join(file_path, file)
        dest_file = join(folder_name, file)

        if not os.path.exists(dest_file):
            shutil.move(src_file, dest_file)

            logging.basicConfig(level=logging.INFO)
            logging.info(f"Moving {src_file} to {dest_file}")
        else:
            new_dest_file = join(folder_name, f"{filename}_i.{filetype}")

            shutil.move(src_file, new_dest_file)
            logging.basicConfig(level=logging.INFO)
            logging.info(f"Moving {src_file} to {dest_file}")

    # Remove empty folders
    for folder in listdir(file_path):
        folder_path = join(file_path, folder)
        if isdir(folder_path) and is_folder_empty(folder_path):
            os.rmdir(folder_path)


except Exception as e:
    print(f"Error processing {file}: {e}")