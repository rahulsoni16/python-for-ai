import os

from dotenv import load_dotenv
from google import genai

try:
    # Load the .env file
    load_dotenv()

    print("GEMINI_API_KEY:", os.environ.get("GEMINI_API_KEY"))

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3.5-flash", contents="What is my name?"
    )
except Exception as e:
    print(f"Error: {e}")


print(response.text)