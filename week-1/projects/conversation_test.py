import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="explain what an Agentic Workflow is and waht would be the responsibilities of that role in an AI-first technology company",
    config = types.GenerateContentConfig(
        system_instruction="you are a career specialist that is up to date to the most reacent research about the topic. Your maind soruces of informaiton are academic articles and the opionion of scholars, you don't rely on general information on the internet, and you never consult sources such as instagram and youtube",
        temperature = 1.5)
)


print(response.text)