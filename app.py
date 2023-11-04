from datetime import timedelta
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = 'seckey12345'
ALGORITHM = 'HS256'
EXPIRATION_TIME = timedelta(minutes=3)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')