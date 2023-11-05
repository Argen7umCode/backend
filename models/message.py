from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    date: datetime = datetime.now()

    conversation_id: Optional[int] = Field(default=None, foreign_key="conversation.id")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")