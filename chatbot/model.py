from typing import Any
from transformers import AutoModel, AutoTokenizer
import torch

model_name = "openlmlab/open-chinese-llama-7b-patch"


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Model(Singleton):
    def __init__(self) -> None: 
        try:
            self.model = AutoModel.from_pretrained('backend/chatbot/model')
        except FileNotFoundError:
            self.model = AutoModel.from_pretrained(model_name)

    def __call__(self, inputs: str) -> Any:
        with torch.no_grad:
            return self.model(**inputs)

class Tokenizer(Singleton):
    def __init__(self) -> None:
        try:
            self.tokenizer = AutoModel.from_pretrained('backend/chatbot/tokenizer')
        except FileNotFoundError:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)

class ChatBot(Singleton):
    def __init__(self, model: Model, 
                 tokenizer: Tokenizer, 
                 system_prompt: str) -> None:
        self.model = model
        self.tokenizer = tokenizer
        self.system_prompt = system_prompt

    def __add_prompt_tamplate(self, user_message: str, 
                              conversation_history: str):
        return self.system_prompt + '\nConversation history:\n' + conversation_history.strip() + \
                                    '\nUser:\n' + user_message.strip() + \
                                    '\nChatbot:\n'
    
    async def get_chatbot_message(self, user_message: str, 
                              conversation_history: str):
        prompt = self.__add_prompt_tamplate(user_message, conversation_history)
        return self.model(self.tokenizer(prompt))



# async def get_prediction(text: str):
#     inputs = tokenizer(text, return_tensors="pt")

#     with torch.no_grad():
#         outputs = model(**inputs)


#     return {"result": "обработанный результат"}
