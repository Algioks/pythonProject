import os
from pprint import pprint
import re
from typing import List, Optional

FUNC = "modified"
DIR = "some_path"


def scan_directory(directory: str, exclude: Optional[List[str]] = None) -> List[str]:
    files_list = []
    try:
        for root, dirs, files in os.walk(directory):
            found_exclude = False

            for exclude_dir in exclude:
                if exclude_dir in root:
                    found_exclude = True
                    break

            if found_exclude:
                continue

            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    files_list.append(file_path)
    except Exception as e:
        print(f"Error while scanning directory: {e}")
    return files_list


def read_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error while reading file '{file_path}': {e}")
        return ""
        
def find_defined_functions(file_content: str) -> List[str]:
    defined_functions = []
    try:
        pattern = re.compile(r"def (\w+)\(")
        matches = pattern.findall(file_content)
        defined_functions = matches
    except Exception as e:
        print(f"Error while finding defined functions: {e}")
    return defined_functions

def find_func():
    directory = r"C:\Programming Projects\pythonProject"  # Your directory here
    exclude_dirs = ["venv", "tests"]  # Directories to exclude

    try:
        files_to_check = scan_directory(directory=directory, exclude=exclude_dirs)
        
        for file_path in files_to_check:
            file_content = read_file(file_path)
            defined_functions = find_defined_functions(file_content)
            
            if defined_functions:
                print(f"Defined functions in '{file_path}': {', '.join(defined_functions)}")
            else:
                print(f"No defined functions found in '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    find_func()
            
            
    # python -m pytest
    
    # lesson 2
    # scan function should return not a filenames but an absolute paths
    # create function that reads a file and check if function is defined in the file https://www.dataquest.io/blog/read-file-python/

    # lesson 3
    # two separate functions to get func defenitions and func calls.
    # add argparser to input the project path.