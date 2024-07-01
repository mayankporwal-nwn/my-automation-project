#!usr/bin/python3
import os
import csv
from datetime import datetime

def generate_file_report(directory, report_file):
    """
    Generates a CSV report file containing information about files in a directory.

    Args:
    - directory (str): Directory path to scan for files.
    - report_file (str): Path to the CSV file where the report will be written.
    """
    # Open the CSV file in write mode, with newline='' to prevent extra newlines
    with open(report_file, 'w', newline='') as csvfile:
        # Define the field names for the CSV header
        fieldnames = ['Filename', 'Size (KB)', 'Last Modified']
        # Create a CSV DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write the header row with field names
        writer.writeheader()

        # Iterate over each file in the specified directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            # Check if the current item in the directory is a file
            if os.path.isfile(filepath):
                # Get the size of the file in kilobytes (KB)
                size = os.path.getsize(filepath) / 1024
                # Get the last modified timestamp and convert it to a datetime object
                last_modified = datetime.fromtimestamp(os.path.getmtime(filepath))
                # Write a row to the CSV file with filename, size, and last modified date
                writer.writerow({'Filename': filename, 'Size (KB)': size, 'Last Modified': last_modified})

if __name__ == "__main__":
    # Example usage:
    
    # Generate a file report for files in the 'organized' directory
    # and save it as 'file_report.csv'
    generate_file_report('organized', 'file_report.csv')
