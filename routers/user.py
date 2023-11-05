from fastapi import APIRouter, Depends, HTTPException, status
from utils import user_creator
from models.user import User

from models.conversation import ConversationModel

user_router = APIRouter()

@user_router.post('api/v1/register')
async def resister_user(username: str, password: str):
    try:
        user = await user_creator(User(username, password))
        return user
    except Exception:
        pass
