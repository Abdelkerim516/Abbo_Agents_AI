from google.ai.generativelanguage_v1beta.types import Content

class SessionService:
    def __init__(self):
        self.sessions = {}

    def get_session(self, user_id):
        if user_id not in self.sessions:
            self.sessions[user_id] = []
        return self.sessions[user_id]

    def add_message(self, user_id, role, text):
        session = self.get_session(user_id)
        session.append(Content(role=role, parts=[Content.Part(text=text)]))
