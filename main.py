import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")



def main() -> None:
    print("Hello from python-ai-agent!")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": "what is the meaning of life?"
            }
        ],
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()