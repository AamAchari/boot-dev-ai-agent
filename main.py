import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


if __name__ == "__main__":
    cmd_arguments = sys.argv
    # print(cmd_arguments)
    user_prompt = cmd_arguments[1]
    verbose_on = cmd_arguments[-1] == '--verbose'
    # genai model to generate the respective response for the content passed
    model = "gemini-2.0-flash-001"
    messages =  [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    ai_response = client.models.generate_content(model=model, contents=messages)
    print(ai_response.text)
    if verbose_on:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {ai_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {ai_response.usage_metadata.candidates_token_count}")