# from sqlmodel import SQLModel, Field, Relationship
# from typing import Optional
# from datetime import datetime

# # Нужно импортировать Message, когда оно будет определено, чтобы избежать циклических импортов
# from .conversation import ConversationModel  # Убедитесь, что это имя модели, а не имя таблицы

# class Message(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     text: str
#     date: datetime = Field(default_factory=datetime.now)  # Использование default_factory

#     # Убедитесь, что имя таблицы 'conversations' соответствует имени в ConversationModel
#     conversation_id: Optional[int] = Field(default=None, foreign_key="conversations.id")
#     user_id: Optional[int] = Field(default=None, foreign_key="users.id")

#     user: 'User' = Relationship(back_populates="messages")
#     conversation: ConversationModel = Relationship(back_populates="messages")
