from fastapi import APIRouter, Depends
from app import verificator

from models.conversation import ConversationModel

router = APIRouter()


@router.post('/conversation')
async def create_conversation(user: str = Depends(verificator.verify_jwt)):
    if user: 
        db_conversation = ConversationModel(user_id=user.id)
        session = 