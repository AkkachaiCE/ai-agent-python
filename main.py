import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


def main():
    load_dotenv()

    if sys.argv[-1] == "--verbose":
        args = sys.argv[1:-1]
        verbose = True
    else:
        verbose = False
        args = sys.argv[1:]

    if not args:
        print('AI Assistant Usage: uv run main.py "your prompt here"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    model = 'gemini-2.0-flash-001'
    user_prompt = " ".join(args)

    # Set User: (role) for prompt message
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(model, client, messages, verbose)

def generate_content(model, client, messages, verbose):
    response = client.models.generate_content(model=model, contents=messages)
    print(f"The response is:\n{response.text}")
    if verbose:
        print(f"User prompt: {messages[0].parts[0].text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    


if __name__ == "__main__":

    main()
