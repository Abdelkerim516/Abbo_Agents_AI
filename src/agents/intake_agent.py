from src.tools.summary_tool import summarize_text

class IntakeAgent:
    def run(self, text):
        return f"Incoming message captured:\n{text}"
