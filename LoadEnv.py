import os

from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get("API_KEY")
debug = os.environ.get("DEBUG")
gemini_api_key = os.environ.get("GEMINI_API_KEY")

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")
print(f"Gemini API Key: {gemini_api_key}")
