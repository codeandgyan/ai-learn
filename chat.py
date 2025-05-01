from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
)

prompt = input("Enter your prompt: ");

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)
print(response.text)
