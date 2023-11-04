from models.db import get_session
from utils.database import get_user_from_db
from app import verificator
from models.user import User

from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post('/login')
async def login(user: User):
    if get_user_from_db(user.username, user.password):
        return {'access_token': verificator.create_jwt({'sub': user.username}), 
                'token_type'  : 'bearer'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    
