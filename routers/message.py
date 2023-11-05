from fastapi import APIRouter, Depends, HTTPException, status
from app import verificator
from app import user_getter, conversation_getter, message_getter
from app import user_creator, conversation_creator, message_creator 

from models.conversation import ConversationModel
from models.user import User
from models.message import Message

router = APIRouter()


@router.post('api/v1/message')
async def create_message(text: str, conversation:ConversationModel, 
                         username: str = Depends(verificator.verify_jwt)):
    if username:
        user = (await user_getter.get_by_username(username))[0]
        message = Message(text = text, conversation_id=conversation.id, user_id=user.id)
        await message_creator.create(message)
        return message
    
@router.get('api/v1/message/{limit}')
async def get_messages_by_username_and_id_from_db(id: int, limit: int=10, 
                                                  username: str = Depends(verificator.verify_jwt)):
    if username:
        user = (await user_getter.get_by_username(username))[0]
        messages = await message_getter.get_by_user_and_id(user, id)
        return messages[:limit]
    
@router.get('api/v1/conversation_messages/')
async def get_messages_by_conversation_id(conversation_id: int, limit: int=10, 
                                          username: str = Depends(verificator.verify_jwt)):
    if username:
        conversation = (await conversation_getter.get_by_id(conversation_id))[0]
        user = (await user_getter.get_by_username(username))[0]
        messages = await message_getter.get_by_conversation(conversation)
        users_ids = set(message.id for message in messages)
        if user.id in users_ids:
            return messages[:limit]
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'No messages were found by conversation_id for this user')
    

