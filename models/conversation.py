from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class ConversationModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    data: datetime = datetime.now()
