schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a python file in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to get content from, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Arguments to be passed to the file that will be run"
                },
            },
            "required": ["file_path"]
        },
    },
}

import os
import subprocess
from functions.helpers import validate_path

def run_python_file(working_directory: str, file_path: str, args: list[str]| None = None) -> str:

    if not file_path.endswith(".py"):
        return f"{file_path} is not a python file"

    # Validate path is within the specified working_directory
    path_validation = validate_path(working_directory, file_path)
    if(path_validation["message"]) != "Success":
        return path_validation["message"]
    else:
        target_dir = path_validation["target_dir"]

    command = ["python", target_dir]
    if args:
        command.extend(args)

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        output = result.stdout
        error = result.stderr
        
        return_message = ""
        
        if result.returncode != 0:
            return_message += f"Process exited with error {result.returncode}.\n"

        if output:
            return_message += f"STDOUT: {output}.\n"

        if error:
            return_message += f"STDERR: {error}.\n"
        
        if not output and not error:
            return_message += "No output produced.\n"

    except subprocess.CalledProcessError as e:
        return f"Error: executing Python file: {e}"

    return return_message