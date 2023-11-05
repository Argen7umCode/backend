from fastapi import APIRouter, Depends, HTTPException, status
from app import verificator
from app import user_getter, conversation_getter, message_message
from app import user_creator, conversation_creator, message_creator 

from models.conversation import ConversationModel
from models.user import User
from models.message import Message

router = APIRouter()


@router.post('/message')
async def create_message(text: str, conversation:ConversationModel, 
                         username: str = Depends(verificator.verify_jwt)):
    if username:
        user = user_getter.get_by_username(username)
        message = Message(text = text, conversation_id=conversation.id, user_id=user.id)
        await message_creator.create(message)
        return message
    
@router.get('/message')
async def get_message(id: int, username: str = Depends(verificator.verify_jwt)):
    if username:
        user = user_getter.get_by_username(username)