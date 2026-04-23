import openai
import json

def authenticate():
    """Loads the API key and authenticates with OpenAI."""
    try:
        with open('GPT-3-SECRET-KEY.json') as f:
            key = json.load(f)
        openai.api_key = key["OPEN_API_KEY"]
        print("Authentication successful.")
    except FileNotFoundError:
        print("Error: 'GPT-3-SECRET-KEY.json' file not found.")
    except KeyError:
        print("Error: 'OPEN_API_KEY' not found in the JSON file.")