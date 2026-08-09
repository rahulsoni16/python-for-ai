import os

from dotenv import load_dotenv
from google import genai

# Load the .env file
load_dotenv()

print("GEMINI_API_KEY:", os.environ.get("GEMINI_API_KEY"))

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Write a short poem about the beauty of nature."
)

print(response.text)