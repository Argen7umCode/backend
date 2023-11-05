from app import ALGORITHM, EXPIRATION_TIME, SECRET_KEY
from utils.getters import UserGetter, ConversationGetter, MessageGetter
from utils.creators import UserCreator, ConversationCreator, MessageCreator
from utils.jwt import Verificator

from datetime import timedelta
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = 'seckey12345'
ALGORITHM = 'HS256'
EXPIRATION_TIME = timedelta(minutes=3)

user_getter, conversation_getter, message_getter = UserGetter(), ConversationGetter(), MessageGetter()
user_creator, conversation_creator, message_creator = UserCreator(), ConversationCreator(), MessageCreator()

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
verificator = Verificator(algorithm=ALGORITHM, 
                          expiration_time=EXPIRATION_TIME, 
                          secret_key=SECRET_KEY)