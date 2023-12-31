from models.models import User
from utils import user_getter, verificator

from fastapi import APIRouter, HTTPException, status

login_router = APIRouter()

@login_router.post('/api/v1/login')
async def login(username: str, password: str):
    db_user = (await user_getter.get_by_username(username))[0]
    if password == db_user.password:
        try:
            return {'access_token': verificator.create_jwt({'sub': str(db_user.id)}), 
                'token_type'  : 'bearer'}
        except Exception:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    