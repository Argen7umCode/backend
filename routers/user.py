from fastapi import APIRouter, Depends, HTTPException, status
from app import verificator
from app import user_getter, conversation_getter, message_message
from app import user_creator, conversation_creator, message_creator 
from models.user import User

from models.conversation import ConversationModel


router = APIRouter()


@router.post('api/v1/register')
async def resister_user(username: str, password: str):
    try:
        user = await user_creator(User(username, password))
    except Exception:
        pass