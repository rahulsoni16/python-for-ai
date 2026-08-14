import os

from dotenv import load_dotenv
from google import genai

# Load the .env file
load_dotenv()

print("GEMINI_API_KEY:", os.environ.get("GEMINI_API_KEY"))


def ask_gemini(prompt):

    client = genai.Client()
    # print("Prompt:", prompt)
    response = client.models.generate_content(model="gemini-3.5-flash", contents=prompt)
    return response.text