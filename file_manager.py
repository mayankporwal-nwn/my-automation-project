#!/usr/bin/python3

# Script to handle file and directory operations.

import os
import shutil
import time

def create_directory(path):
    """
    Creates a directory if it does not already exist.

    Args:
    - path (str): Directory path to be created.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def move_files(source_dir, target_dir, extension):
    """
    Moves files with a specific extension from source directory to target directory.

    Args:
    - source_dir (str): Source directory containing files to move.
    - target_dir (str): Destination directory where files will be moved.
    - extension (str): File extension (e.g., '.pdf') to filter files for moving.
    """
    for filename in os.listdir(source_dir):
        if filename.endswith(extension):
            shutil.move(os.path.join(source_dir, filename), target_dir)

def delete_old_files(directory, days):
    """
    Deletes files in a directory that are older than a specified number of days.

    Args:
    - directory (str): Directory path where files will be checked and deleted.
    - days (int): Number of days. Files older than this will be deleted.
    """
    now = time.time()
    cutoff = now - (days * 86400)  # Calculating cutoff timestamp (in seconds)

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and os.path.getmtime(filepath) < cutoff:
            os.remove(filepath)

if __name__ == "__main__":
    # Example usage:
    
    # Ensure 'organized' directory exists or create it
    create_directory('organized')
    
    # Move PDF files from 'downloads' directory to 'organized' directory
    move_files('downloads', 'organized', '.pdf')
    
    # Delete files in 'organized' directory that are older than 30 days
    delete_old_files('organized', 30)
