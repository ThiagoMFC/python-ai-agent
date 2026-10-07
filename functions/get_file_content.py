import os
from helpers import validate_path

def get_file_content(working_directory: str, file_path: str) -> str:

    # Validate path is within the specified working_directory
    path_validation = validate_path(working_directory, file_path, "file")
    if(path_validation["message"]) != "Success":
        print(path_validation["message"])
        return
    else:
        target_dir = path_validation["target_dir"]

    is_file = os.path.isfile(target_dir)

    if not is_file:
        print(f"{file_path} is not a file")
    else:
        print(target_dir) 


get_file_content("calculator/pkg", "calculat.py")