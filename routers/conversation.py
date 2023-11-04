from fastapi import APIRouter, Depends
from app import verificator

from chatbot.conversation import Conversation
from models.conversation import ConversationModel

router = APIRouter()


@router.get('/protected_resource')
async def get_resource(user: str = Depends(verificator.verify_jwt)):
    if user:
        chat_conversation = Conversation(10)
        db_conversation = ConversationModel(user_id=user.id)