from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String
from typing import Optional
from datetime import datetime
from typing import List, Optional


class Message(SQLModel, table=True):
    __tablename__ = 'messages' 
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    date: datetime = Field(default_factory=datetime.now)  # Использование default_factory

    # Убедитесь, что имя таблицы 'conversations' соответствует имени в ConversationModel
    conversation_id: Optional[int] = Field(default=None, foreign_key="conversations.id")
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")


class User(SQLModel, table=True):
    __tablename__ = 'users' 
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column("username", String, unique=True))
    password: str = Field(sa_column=Column("password", String, unique=True))

    conversations: List["ConversationModel"] = Relationship(back_populates="users", link_model=Message)


class ConversationModel(SQLModel, table=True):
    __tablename__ = 'conversations'  # Устанавливаем явно имя таблицы, если нужно
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(default_factory=datetime.now)  # Используем default_factory

    users: List[User] = Relationship(back_populates="conversations", link_model=Message)
