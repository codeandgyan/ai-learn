from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY"),
)

text = "I love software engineering"

result = client.models.embed_content(model="gemini-embedding-exp-03-07", contents=text)

print("Embedding:", result.embeddings)
