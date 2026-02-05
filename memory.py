class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_user(self, message):
        self.history.append({"role": "user", "parts": [message]})

    def add_model(self, message):
        self.history.append({"role": "model", "parts": [message]})

    def get(self):
        return self.history
