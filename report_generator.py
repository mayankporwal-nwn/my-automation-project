import os
import csv
from datetime import datetime

def generate_file_report(directory, report_file):
    with open(report_file, 'w', newline='') as csvfile:
        fieldnames = ['Filename', 'Size (KB)', 'Last Modified']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                size = os.path.getsize(filepath) / 1024  # Size in KB
                last_modified = datetime.fromtimestamp(os.path.getmtime(filepath))
                writer.writerow({'Filename': filename, 'Size (KB)': size, 'Last Modified': last_modified})

if __name__ == "__main__":
    generate_file_report('organized', 'file_report.csv')