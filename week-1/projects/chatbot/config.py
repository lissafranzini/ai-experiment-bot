import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("GEMINI_API_KEY")
MODEL="gemini-2.5-flash"
TEMPERATURE=0.3
SYSTEM_INSTRUCTION="you are a helpful chatbot that answers to questions in a straightforwrad way. No guesses, if you don't know something, you'll just tell the user you don't know."