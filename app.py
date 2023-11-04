from app import ALGORITHM, EXPIRATION_TIME, SECRET_KEY
from utils.jwt import Verificator

from datetime import timedelta
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = 'seckey12345'
ALGORITHM = 'HS256'
EXPIRATION_TIME = timedelta(minutes=3)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
verificator = Verificator(algorithm=ALGORITHM, 
                          expiration_time=EXPIRATION_TIME, 
                          secret_key=SECRET_KEY)