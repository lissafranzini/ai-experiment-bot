import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
                      
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="You are a helpful assistant. When answering questions, always state your confidence level (high, medium, or low). If you are not certain about specific numbers or dates, say so. Never present estimates as exact figures. How many people work at Genesys Telecommunications?"
)

print(response.text)
