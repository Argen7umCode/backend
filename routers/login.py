from app import app, oauth2_scheme, SECRET_KEY, EXPIRATION_TIME, ALGORITHM
from models.db import get_session
from models.user import User


from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from datetime import datetime
import jwt


def get_user_from_db(username: str, password: str):
    query = select(User).where(User.username == username and User.password == password)


def create_jwt(data: dict):
    data['exp'] = datetime.utcnow() + EXPIRATION_TIME
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def verify_jwt(token: str = Depends(oauth2_scheme)):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get('sub')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired Signature Error")
    except jwt.PyJWKError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")


@app.post('/login')
async def login(user: User):
    if get_user_from_db(user.username, user.password):
        return {'access_token': create_jwt({'sub': user.username}), 
                'token_type'  : 'bearer'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    
@app.get('/protected_resource')
async def get_resource(user: str = Depends(verify_jwt)):
    if user:
        return {
            'message' : 'Acces to the protected resourse is allowed'
        }