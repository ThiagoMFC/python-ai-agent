import os

# Allow the LLM agent to specify which directory it wants to scan, but the working_directory will be pre-set
# to limit the scope of directories and files that the LLM is able to view
def get_files_info(working_directory: str, directory: str= ".")-> str:

    if not os.path.isdir(directory):
        return f"Error: {directory} is not a directory"
    
    # Validate path is within the specified working_directory
    try:
        wd_absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(wd_absolute_path, directory))
        valid_targer_dir = os.path.commonpath([wd_absolute_path, target_dir]) == wd_absolute_path
    except:
        return f"Error: could not validate working directory path"

    if not valid_targer_dir:
        return f"Error: Cannot list {directory} as it's outside of permitted working directory"

    return f"Success: {directory} is within the working directory"


get_files_info("calculator")