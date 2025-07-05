import os
from dotenv import load_dotenv
from google import genai
import sys


def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print('AI Assistant Usage: uv run main.py "your prompt here"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    model = 'gemini-2.0-flash-001'
    contents = " ".join(args)

    response = client.models.generate_content(model=model, contents=contents)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"The response is:\n{response.text}")
    

if __name__ == "__main__":

    main()
