import os
import shutil
import sys
from pathlib import Path
from clean_folder.WORCK_6 import main as process_worck_6

def copy_file_to_target(source_file, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    try:
        shutil.copy(source_file, target_directory)
        print(f"File {source_file} successfully copied to {target_directory}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: clean-folder <source_file> <target_directory>")
        sys.exit(1)

    source_file = sys.argv[1]
    target_directory = sys.argv[2]

    copy_file_to_target(source_file, target_directory)

    # Process the WORCK_6.py file
    process_worck_6()

if __name__ == "__main__":
    main()
