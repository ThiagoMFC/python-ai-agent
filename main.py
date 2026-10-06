import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def main():

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": "why is the sky blue? one paragraph maximum"
            }
        ],
    )

    if response is None or response.usage is None:
        print("bad response")
        return

    print(f"usage tokens: {response.usage.prompt_tokens}")
    print(f"response tokens: {response.usage.completion_tokens}")

    print(response.choices[0].message.content)

main()