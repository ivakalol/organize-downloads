from os import listdir
from os.path import isfile, join, isdir
import os
import shutil
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

def is_folder_empty(folder_path):
    """Check if a folder is empty."""
    return len(listdir(folder_path)) == 0

try:
    # Path to organize
    file_path = r"C:\Users\Ivaka2\Downloads"
    logging.info("Starting to organize files in: %s", file_path)
    
    # Get all files in the directory
    files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    logging.info("Found %d file(s) to process.", len(files))

    for file in files:
        try:
            filename, filetype = os.path.splitext(file)
            filetype = filetype[1:].lower()

            # Create folder for file type if it doesn't exist
            folder_name = join(file_path, filetype if filetype else "no_extension")
            if not isdir(folder_name):
                os.mkdir(folder_name)
                logging.info("Created folder: %s", folder_name)

            # Move the file
            src_file = join(file_path, file)
            dest_file = join(folder_name, file)

            if not os.path.exists(dest_file):
                shutil.move(src_file, dest_file)
                logging.info("Moved file: %s -> %s", src_file, dest_file)
            else:
                new_dest_file = join(folder_name, f"{filename}_i.{filetype}")
                shutil.move(src_file, new_dest_file)
                logging.info("File already exists. Renamed and moved: %s -> %s", src_file, new_dest_file)
        except Exception as file_error:
            logging.error("Error processing file '%s': %s", file, file_error)

    # Remove empty folders
    logging.info("Checking for empty folders to remove...")
    for folder in listdir(file_path):
        try:
            folder_path = join(file_path, folder)
            if isdir(folder_path) and is_folder_empty(folder_path):
                os.rmdir(folder_path)
                logging.info("Removed empty folder: %s", folder_path)
        except Exception as folder_error:
            logging.error("Error removing folder '%s': %s", folder, folder_error)

    logging.info("File organization completed successfully.")

except Exception as e:
    logging.error("Unexpected error: %s", e)
