schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns contents of a file in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to get content from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

import os
from functions.helpers import validate_path
from dotenv import load_dotenv

load_dotenv()
max_chars = int(os.environ.get("MAX_CHARS"))

def get_file_content(working_directory: str, file_path: str) -> str:

    # Validate path is within the specified working_directory
    path_validation = validate_path(working_directory, file_path)
    if(path_validation["message"]) != "Success":
        #print(path_validation["message"])
        return path_validation["message"]
    else:
        target_dir = path_validation["target_dir"]
        #print(target_dir)


    with open(target_dir, "r") as file:
        file_content = file.read(max_chars)
        if len(file_content) == max_chars:
            file_content += f"...\n[... File {file_path} truncated ad {max_chars} characters]"

    #print(file_content)
    return file_content


get_file_content("calculator/pkg", "calculator.py")