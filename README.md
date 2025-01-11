# Organize Downloads Script

This project includes two files to help organize and manage files in the `Downloads` directory. The batch file ensures easy execution of the Python script, which organizes files into folders based on their file types.

## Files

### 1. **`run_script.bat`**
- **Description**: A batch file to execute the Python script with minimal effort.
- **Contents**:
  ```batch
  @echo off
  python "C:\Git Hub\organize-downloads\Scrypt.py"
  pause
  ```
- **Purpose**: Automates the execution of the Python script.

### 2. **`Scrypt.py`**
- **Description**: A Python script that organizes files in the `Downloads` directory into folders based on their file types.
- **Key Features**:
  - Files are moved into folders named after their file types (e.g., `.pdf` files go to `pdf_folder`).
  - If a file with the same name already exists, the script appends `_i` to the new file's name to prevent overwriting.
  - Automatically creates folders for new file types.
  - Removes empty folders in the `Downloads` directory.

- **Code Overview**:
  ```python
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
  ```

## How to Use

### Prerequisites
- Python installed on your system (ensure the `python` command is available in your terminal).

### Steps to Run
1. Place both files (`run_script.bat` and `Scrypt.py`) in the same directory.
2. Update the `file_path` in `Scrypt.py` to point to your actual `Downloads` directory.
3. Double-click on `run_script.bat` to execute the script.
4. The `Downloads` folder will now be organized, with files moved to their respective folders.

### Output
- Files will be moved into folders named after their file types.
- Empty folders in the `Downloads` directory will be removed.

## Notes
- Ensure you have permission to modify the `Downloads` directory and its contents.
- Existing files in type folders will not be overwritten; the new files will have `_i` appended to their names.
- If you encounter any issues, ensure that Python is correctly installed and the script's paths are correctly configured.

## License
This project is free to use and distribute. Modify it as needed for your personal use!
