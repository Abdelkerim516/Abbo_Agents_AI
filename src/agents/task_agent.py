import google.generativeai as genai
from src.config import GEMINI_API_KEY

class TaskAgent:
    def run(self, summary):
        model = genai.GenerativeModel("models/gemini-flash-latest")
        response = model.generate_content(f"""
Convert this summary into a list of tasks in JSON:
{summary}
""")
        return response.text
