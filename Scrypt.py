from os import listdir
from os.path import isfile, join, isdir
import os
import shutil
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(message)s\n")

def is_folder_empty(directory_path):
    """Check if a directory is empty."""
    return len(listdir(directory_path)) == 0

try:
    # Path to organize
    downloads_directory = r"C:\Users\yourUser\Downloads"
    logging.info("Starting to organize files in: %s", downloads_directory)
    
    # Get all files in the directory
    all_files = [file for file in listdir(downloads_directory) if isfile(join(downloads_directory, file))]
    logging.info("Found %d file(s) to process.", len(all_files))

    for current_file in all_files:
        try:
            base_name, extension = os.path.splitext(current_file)
            extension = extension[1:].lower()  # Remove the dot and normalize to lowercase

            # Create a folder for the file type if it doesn't exist
            folder_for_extension = join(downloads_directory, extension if extension else "no_extension")
            if not isdir(folder_for_extension):
                os.mkdir(folder_for_extension)
                logging.info("Created folder: %s", folder_for_extension)

            # Move the file
            source_path = join(downloads_directory, current_file)
            destination_path = join(folder_for_extension, current_file)

            if not os.path.exists(destination_path):
                shutil.move(source_path, destination_path)
                logging.info("Moved file: %s -> %s", source_path, destination_path)
            else:
                renamed_destination_path = join(folder_for_extension, f"{base_name}_i.{extension}")
                shutil.move(source_path, renamed_destination_path)
                logging.info("File already exists. Renamed and moved: %s -> %s", source_path, renamed_destination_path)
        except Exception as file_error:
            logging.error("Error processing file '%s': %s", current_file, file_error)

    # Remove empty folders
    logging.info("Checking for empty folders to remove...")
    for directory in listdir(downloads_directory):
        try:
            directory_path = join(downloads_directory, directory)
            if isdir(directory_path) and is_folder_empty(directory_path):
                os.rmdir(directory_path)
                logging.info("Removed empty folder: %s", directory_path)
        except Exception as folder_error:
            logging.error("Error removing folder '%s': %s", directory, folder_error)

    logging.info("File organization completed successfully.")

except Exception as e:
    logging.error("Unexpected error: %s", e)
