import google.generativeai as genai
from src.config import GEMINI_API_KEY

def summarize_text(text):
    model = genai.GenerativeModel("models/gemini-flash-latest")
    response = model.generate_content(f"Summarize this:\n{text}")
    return response.text
