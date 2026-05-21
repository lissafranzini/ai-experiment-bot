from google import genai
from google.genai import types
from google.genai import errors
from config import MODEL, SYSTEM_INSTRUCTION, TEMPERATURE
from config import API_KEY

client = genai.Client(api_key = API_KEY)


def ai_client (prompt):
    response = client.models.generate_content(
                model = MODEL,
                contents = prompt,
                config = types.GenerateContentConfig(
                system_instruction= SYSTEM_INSTRUCTION,
                temperature = TEMPERATURE))
    return response

def handle_client_error (e):
    error_text = str(e)
    if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
        print("Quota exceeded: you have reached the Gemini API limit for your current plan.")
        return "quota exceeded"
    else:
        return e


