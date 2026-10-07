import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def main():

    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    if response is None or response.usage is None:
        print("bad response")
        return

    if args.verbose is True:
        print(f"usage tokens: {response.usage.prompt_tokens}")
        print(f"response tokens: {response.usage.completion_tokens}")
        print(f"User prompt: {args.user_prompt}")
        print(f"Response: {response.choices[0].message.content}")
    else:
        print(f"Response: {response.choices[0].message.content}")


main()