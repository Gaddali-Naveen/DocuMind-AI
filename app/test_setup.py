from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API Key Found:", bool(api_key))
print("DocuMind AI Setup Successful")