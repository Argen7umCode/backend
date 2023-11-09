from fastapi import APIRouter, Depends, HTTPException, status
from utils import user_creator
from models.models import User, ConversationModel
from asyncpg.exceptions import UniqueViolationError

user_router = APIRouter()

@user_router.post('/api/v1/register')
async def resister_user(username: str, password: str):
    user = User(username=username, password=password)
    try:
        db_user = await user_creator.create(user)
    except UniqueViolationError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='The username or password are occupied')
    return db_user

