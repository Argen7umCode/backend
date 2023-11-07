from fastapi import APIRouter, Depends, HTTPException, status
from utils import user_creator
from models.models import User, ConversationModel


user_router = APIRouter()

@user_router.post('/api/v1/register')
async def resister_user(username: str, password: str):
    user = User(username=username, password=password)
    db_user = await user_creator.create(user)
    print(db_user)
    return db_user

