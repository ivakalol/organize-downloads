from os import listdir
from os.path import isfile, join 
import os
import shutil

file_path = "C:\Users\Ivaka2\Downloads"
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

file_list =[]

for file in files:
    
    filename = file.split(".")[0]
    filetype = file.split(".")[1]
   
    # manage Folders
    if filetype not in file_list:
        file_list.append(filetype)
        new_folder_name = filetype + "/" + '_folder'

        if os.path.isdir(new_folder_name) == False:
            os.mkdir(new_folder_name)
            folder_name = new_folder_name
        else:
            folder_name = file_path + "/" + '_folder'
    

    
        