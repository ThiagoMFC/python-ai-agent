import os
import argparse
import json
from dotenv import load_dotenv
from openai import OpenAI
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Run Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
]

def main():

    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(10):

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        if response is None or response.usage is None:
            print("Agent unavailable")
            return

        message = response.choices[0].message
        result_message = ""

        if args.verbose is True:
            print(f"usage tokens: {response.usage.prompt_tokens}")
            print(f"response tokens: {response.usage.completion_tokens}")
            print(f"User prompt: {args.user_prompt}")
            print(f"Response: {message.content}")
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    function_args = json.loads(tool_call.function.arguments or "{}")
                    #print(f"Calling function: {tool_call.function.name}({function_args})")
                    result_message = call_function(tool_call, args.verbose)
            else:
               print(message.content)
               return
        else:
            print(f"Response: {message.content}")
            result_message = call_function(message.tool_calls)

        if not result_message["content"]:
            print("bad response")
            return

        #print(f"-> {result_message["content"]}")

        #make model is aware of conversation
        messages.append(message)
        #make model aware of tool call results
        messages.append(result_message)


main()