from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import conint
from utils import conversation_creator, user_getter, conversation_getter, verificator
from models.models import ConversationModel


conversation_router = APIRouter()    

@conversation_router.post(path='/api/v1/conversation')
async def create_conversation(user_id: int = Depends(verificator.verify_jwt)):
    if user_id: 
        db_conversation = ConversationModel(user_id= user_id)
        await conversation_creator.create(db_conversation)
        return db_conversation


@conversation_router.get(path='/api/v1/conversation/')
async def get_conversation_by_user_id(id: Optional[conint(ge=0)] = None, 
                                      user_id: int = Depends(verificator.verify_jwt)):
    user = (await user_getter.get_by_id(user_id))[0]
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    conversations = await conversation_getter.get_by_user(user)
    print(conversations)
    if id is None: 
        return conversations
    try:
        return conversations[id]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='Conversation of the specified id was not found')

