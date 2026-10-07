import os

def validate_path(working_directory: str, directory: str):

    #return_message = []
    return_message = {}

    try:
        wd_absolute_path = os.path.abspath(working_directory)

        if not os.path.isdir(os.path.join(wd_absolute_path, directory)):
            #return_message.append(f"Error: {directory} is not in the working directory")
            return_message["message"] = f"Error: {directory} is not in the working directory"
            return return_message

        target_dir = os.path.normpath(os.path.join(wd_absolute_path, directory))

        valid_target_dir = os.path.commonpath([wd_absolute_path, target_dir]) == wd_absolute_path

    except:
        #return_message.append("Error: could not validate working directory path")
        return_message["message"] = "Error: could not validate working directory path"
        return return_message
    
    if not valid_target_dir:
        #return_message.append(f"Error: Cannot list {directory} as it's outside of permitted working directory")
        return_message["message"] = f"Error: Cannot list {directory} as it's outside of permitted working directory"
        return return_message

    #return_message.append("Success")
    #return_message.append(wd_absolute_path)
    #return_message.append(target_dir)
    #return_message.append(valid_targer_dir)
    return_message["message"] = "Success"
    return_message["target_dir"] = target_dir
    return_message["valid_target_dir"] = valid_target_dir


    return return_message