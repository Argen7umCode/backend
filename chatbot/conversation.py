class Conversation:
    def __init__(self, max_history=5):
        self.max_history = max_history
        self.history = []

    def __add_message(self, message):
        self.history.append(message)
        self.history = self.history[-self.max_history:]

    def add_chatbot_message(self, message):
        message = 'Assistant: ' + message
        self.__add_message(message)

    def add_user_message(self, message):
        message = 'User: ' + message
        self.__add_message(message)    

    def get_history(self):
        return " ".join(self.history)
