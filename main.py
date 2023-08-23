# input is name of the function
import os
from pprint import pprint
from typing import List, Optional

FUNC = "modified"
DIR = "some_path"


def scan_directory(directory: str, exclude: Optional[List[str]] = None) -> List[str]:
    files_list = []
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
                files_list.append(file)
    return files_list


if __name__ == '__main__':
    pprint(
        scan_directory(
            directory=r"C:\Users\andrius.vaitkunas\PycharmProjects\pythonProject",
            exclude=["venv", "tests"]
        )
    )
    # scan function should return not a filenames but an absolute paths
    # create function that reads a file and check if function is defined in the file https://www.dataquest.io/blog/read-file-python/