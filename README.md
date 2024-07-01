# Automated File Management and Reporting System

## Project Overview

The **Automated File Management and Reporting System** is designed to automate file management tasks and generate detailed reports about files in specific directories using Python scripting. This project leverages operating system interaction for file operations and Git/GitHub for version control and collaboration.

### Key Features

1. **File Organization:**
   - **Creating Directories:** Automatically create directories if they do not exist.
   - **Moving Files:** Move files from one directory to another based on file extensions.
   - **Deleting Old Files:** Automatically delete files that are older than a specified number of days to keep directories clean and organized.

2. **Report Generation:**
   - **File Report:** Generate a CSV report listing files in a specified directory with their sizes (in KB) and last modified dates.

### Components

- **file_manager.py:** Handles file operations such as creating directories, moving files based on extensions, and deleting old files.
- **report_generator.py:** Generates a CSV report that lists filenames, sizes, and last modified dates of files in a directory.

## Usage

### Setup

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd my-automation-project
   ```

2. **Python Environment:**
   - Ensure Python 3.x is installed on your system.

#### Running `file_manager.py`

- **Description:**
  - `file_manager.py` automates file organization and cleanup tasks.

- **Command:**
  ```bash
  python file_manager.py
  ```

- **Functionality:**
  - Creates an 'organized' directory if it does not exist.
  - Moves PDF files from 'downloads' to 'organized'.
  - Deletes files older than 30 days in 'organized'.

#### Running `report_generator.py`

- **Description:**
  - `report_generator.py` generates a CSV report listing file details.

- **Command:**
  ```bash
  python report_generator.py
  ```

- **Functionality:**
  - Scans 'organized' directory.
  - Generates `file_report.csv` with filenames, sizes (in KB), and last modified dates.

### Example Usage Scenarios

#### Automating Downloads Folder Organization

- **Description:**
  - Automatically organizes files by type and removes old files from the downloads folder.

- **Usage:**
  - Run `file_manager.py` script to organize and clean up 'downloads' directory.

#### Generating Inventory Reports

- **Description:**
  - Creates detailed reports of files in directories for inventory or auditing purposes.

- **Usage:**
  - Run `report_generator.py` script to generate a CSV report (`file_report.csv`) of files in the 'organized' directory.

#### Contribution
- **Feel free to fork this repository and contribute via pull requests. Contributions are welcome to enhance functionality, fix bugs, or add new features.**
