import os

# Allow the LLM agent to specify which directory it wants to scan, but the working_directory will be pre-set
# to limit the scope of directories and files that the LLM is able to view
def get_files_info(working_directory: str, directory: str= ".")-> str:
    
    # Validate path is within the specified working_directory
    try:
        wd_absolute_path = os.path.abspath(working_directory)
        if not os.path.isdir(os.path.join(wd_absolute_path, directory)):
            return f"Error: {directory} is not a directory"
        target_dir = os.path.normpath(os.path.join(wd_absolute_path, directory))
        valid_targer_dir = os.path.commonpath([wd_absolute_path, target_dir]) == wd_absolute_path
    except:
        return "Error: could not validate working directory path"

    if not valid_targer_dir:
        return f"Error: Cannot list {directory} as it's outside of permitted working directory"

    #return f"Success: {directory} is within the working directory"

    dir_contents = os.listdir(target_dir)
    final_response = ""
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



get_files_info("calculator")