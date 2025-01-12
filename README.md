
# File Organizer Script

This Python script organizes files in a specified directory by moving them into subfolders based on their file extensions. It's especially useful for keeping directories like the Downloads folder tidy.

## Features
- Automatically creates folders for each file extension.
- Moves files into their respective folders.
- Handles duplicate file names by renaming duplicates with a suffix.
- Removes empty folders after organizing files.
- Logs detailed information about the process, including file movements, folder creation, and errors.

## Requirements
- Python 3.x
- Required modules: `os`, `shutil`, and `logging`.

## How It Works
1. The script scans the specified directory for all files.
2. For each file:
   - It determines the file extension.
   - It creates a folder named after the file extension (e.g., `.txt` files go into a `txt` folder).
   - Moves the file into the corresponding folder.
   - If a file with the same name already exists in the destination folder, it renames the file by appending `_i` to the name.
3. After processing all files, it removes any empty folders in the directory.

## Logging
The script uses Python’s logging module to provide real-time feedback. Logs include:
- Folder creation.
- File movement and renaming.
- Empty folder removal.
- Error handling for problematic files or folders.

## Usage
1. Clone or download this repository.
2. Update the `downloads_directory` variable in the script with the path of the directory you want to organize.
3. Run the script:
   ```bash
   python Scrypt.py
   ```

## Example
Given the following files in the `Downloads` folder:
```
example.txt
image.png
document.pdf
example (duplicate).txt
```

After running the script:
```
Downloads/
├── txt/
│   ├── example.txt
│   ├── example_i.txt
├── png/
│   ├── image.png
├── pdf/
│   ├── document.pdf
```

Empty folders will be removed automatically.

## Error Handling
- If the script encounters a file or folder it cannot process, it logs an error but continues execution.
- Example errors include permission issues or invalid file paths.

## Customization
- **Directory to Organize**: Modify the `downloads_directory` variable to target a different folder.
- **Logging Format**: Adjust the `logging.basicConfig()` settings to customize log verbosity or format.
