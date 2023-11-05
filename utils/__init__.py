from .creators import UserCreator, ConversationCreator, MessageCreator
from .getters import UserGetter, ConversationGetter, MessageGetter
from .verification import Verificator
from datetime import timedelta


user_getter, conversation_getter, message_getter = UserGetter(), ConversationGetter(), MessageGetter()
user_creator, conversation_creator, message_creator = UserCreator(), ConversationCreator(), MessageCreator()


SECRET_KEY = 'seckey12345'
ALGORITHM = 'HS256'
EXPIRATION_TIME = timedelta(minutes=3)

verificator = Verificator(algorithm=ALGORITHM, 
                          expiration_time=EXPIRATION_TIME, 
                          secret_key=SECRET_KEY)