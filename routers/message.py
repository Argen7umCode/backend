from utils import message_creator, user_getter, message_getter, conversation_getter, verificator
from models.models import ConversationModel,Message

from fastapi import APIRouter, Depends, HTTPException, status


message_router = APIRouter()
 
@message_router.post('/api/v1/message')
async def create_message(text: str, conversation_id:int, 
                         user_id: str = Depends(verificator.verify_jwt)):
        try:
            user = (await user_getter.get_by_id(int(user_id)))[0][0]
        except Exception: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        message = Message(text = text, 
                          conversation_id=conversation_id, 
                          user_id=user.id)
        await message_creator.create(message)
        return message
    
@message_router.get('/api/v1/conversation_messages/')
async def get_messages_by_conversation_id(conversation_id: int, limit: int = 0, 
                                          user_id: str = Depends(verificator.verify_jwt)):
    if user_id:
        user = (await user_getter.get_by_id(int(user_id)))[0]
        conversation = (await conversation_getter.get_by_id(conversation_id))[0]
        messages = (await message_getter.get_by_conversation(conversation))[0]
        users_ids = set(message.id for message in messages)
        if user.id in users_ids:
            return messages[:limit]
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'No messages were found by conversation_id for this user')
    
