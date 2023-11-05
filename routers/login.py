from models.user import User
from utils import user_getter, verificator

from fastapi import APIRouter, HTTPException, status

login_router = APIRouter()

@login_router.post('/login')
async def login(user: User):
    db_user = await user_getter.get_by_username(user.username)
    if user == db_user:
        return {'access_token': verificator.create_jwt({'sub': user.username}), 
                'token_type'  : 'bearer'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    