schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write/overwrite a file in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to get content from, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "Content to be written to the file"
                },
            },
        },
    },
}

import os
from functions.helpers import validate_path

def write_file(working_directory: str, file_path:str, content:str):

    # Validate path is within the specified working_directory
    path_validation = validate_path(working_directory, file_path)
    if(path_validation["message"]) != "Success":
        #print(path_validation["message"])
        message = f"Error: Cannot write to file {file_path}. "
        return message + path_validation["message"]
    else:
        target_dir = path_validation["target_dir"]

    try:
        with open(target_dir, "w") as file:
            file.write(content)
        message = f"Success: wrote to {file_path}. ({len(content)} characters written) "
    except:
        message = f"Error: unable to write to {file_path}"

    return message


        