import google.generativeai as genai
from src.config import GEMINI_API_KEY

class SupportAgent:
    def run(self, summary):
        model = genai.GenerativeModel("models/gemini-flash-latest")
        response = model.generate_content(f"""
Write a clear, friendly customer support reply based on:
{summary}
""")
        return response.text
