from fastapi import APIRouter, Depends, HTTPException, status
from app import verificator
from app import user_getter, conversation_getter, message_message
from app import user_creator, conversation_creator, message_creator 

from models.conversation import ConversationModel


router = APIRouter()


@router.post('api/v1/conversation')
async def create_conversation(user: str = Depends(verificator.verify_jwt)):
    if user: 
        db_conversation = ConversationModel(user_id= user.id)
        await conversation_creator.create(db_conversation)
        return db_conversation

@router.get('api/v1/conversation/{id}')
async def get_conversation_by_username(id: int = None, username: str = Depends(verificator.verify_jwt)):
    if username: 
        user = user_getter.get_by_username(username)
        conversations = await conversation_getter.get_by_user(user)
        if id is not None: 
            try:
                return conversations[id]
            except IndexError:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                    detail='Conversation of the specified id was not found')
        return conversations