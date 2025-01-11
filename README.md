# Organize Downloads Script

This project includes two files to help organize and manage files in the `Downloads` directory. The batch file ensures easy execution of the Python script, which organizes files into folders based on their file types.

## Files

### 1. **`run_script.bat`**
- **Description**: A batch file to execute the Python script with minimal effort.
- **Make it run**:
  ```batch
  in the .bat file you should edit this:
  python "C:\your\path\to\Scrypt.py"

  while in the python file you should edit your downloads directory
  ```
- **Purpose**: Automates the execution of the Python script.

### 2. **`Scrypt.py`**
- **Description**: A Python script that organizes files in the `Downloads` directory into folders based on their file types.
- **Key Features**:
  - Files are moved into folders named after their file types (e.g., `.pdf` files go to `pdf_folder`).
  - If a file with the same name already exists, the script appends `_i` to the new file's name to prevent overwriting.
  - Automatically creates folders for new file types.
  - Removes empty folders in the `Downloads` directory.

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
