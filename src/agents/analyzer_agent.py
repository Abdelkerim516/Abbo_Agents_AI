import google.generativeai as genai
from src.config import GEMINI_API_KEY

class AnalyzerAgent:
    def run(self, text):
        model = genai.GenerativeModel("models/gemini-flash-latest")
        response = model.generate_content(
            f"Summarize this message in 3 bullet points:\n{text}"
        )
        return response.text
