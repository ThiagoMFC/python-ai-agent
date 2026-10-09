import json
from collections.abc import Callable
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(tool_call, verbose: bool = False) -> dict:

    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    # set the working directory the LLM has access to
    function_args["working_directory"] = "./calculator"

    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
    # etc.
    }

    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }


    # call the function in the map
    result = function_map[function_name](**function_args)

    print({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    })
    
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }