import google.generativeai as genai
from src.config import GEMINI_API_KEY

class ClassifierAgent:
    def run(self, message):
        model = genai.GenerativeModel("models/gemini-flash-latest")
        response = model.generate_content(f"""
Classify into: email, task, or support.
Output only one word.
Message:
{message}
""")
        return response.text.strip().lower()
