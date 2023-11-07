# from sqlmodel import SQLModel, Field, Relationship
# from typing import Optional
# from datetime import datetime

# class ConversationModel(SQLModel, table=True):
#     __tablename__ = 'conversations'  # Устанавливаем явно имя таблицы, если нужно
#     id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: Optional[int] = Field(default=None, foreign_key="users.id")
#     date: datetime = Field(default_factory=datetime.now)  # Используем default_factory

#     user: 'User' = Relationship(back_populates="conversations")
