schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
            "required": ["directory"]
        },
    },
}

import os
from functions.helpers import validate_path

# Allow the LLM agent to specify which directory it wants to scan, but the working_directory will be pre-set
# to limit the scope of directories and files that the LLM is able to view

def get_files_info(working_directory: str, directory: str= ".")-> str:

    final_response = ""
    # Validate path is within the specified working_directory
    path_validation = validate_path(working_directory, directory)
    if(path_validation["message"]) != "Success":
        return path_validation["message"]
    else:
        target_dir = path_validation["target_dir"]

    if not os.path.isdir(target_dir):
        final_response = f"Error: {directory} is not a directory"
        return final_response
    
    dir_contents = os.listdir(target_dir)

    for content in dir_contents:
        try:
            is_dir = os.path.isdir(os.path.join(target_dir, content))
            size = os.path.getsize(os.path.join(target_dir, content))
            name = content
            data = f"- {name}: file_size: {size} bytes, is_dir={is_dir}\n"
            final_response += data
        except:
            return "Error: could not parse directory contents"

    return final_response



#get_files_info("calculator")