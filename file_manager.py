#!/usr/bin/python3

# Script to handle file and directory operations.

import os
import shutil
import time  

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_files(source_dir, target_dir, extension):
    for filename in os.listdir(source_dir):
        if filename.endswith(extension):
            shutil.move(os.path.join(source_dir, filename), target_dir)

def delete_old_files(directory, days):
    now = time.time()
    cutoff = now - (days * 86400)

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and os.path.getmtime(filepath) < cutoff:
            os.remove(filepath)

if __name__ == "__main__":
    create_directory('organized')
    move_files('downloads', 'organized', '.pdf')
    delete_old_files('organized', 30)