from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import User
from models.conversation import ConversationModel
from models.message import Message
from db import Session

from typing import Any
from sqlmodel import SQLModel

class SessionMixin(Session):
    pass


class Creator(SessionMixin):

    async def create(self, item: Any):
        session = await self.get_session()
        session.add(item)
        await session.commit()
        return item

class ConversationCreator(Creator):
    pass

class MessageCreator(Creator):
    pass

class UserCreator(Creator):
    pass



class Getter(SessionMixin):

    async def __get(self, query):
        session = await self.get_session()
        return (await session.execute(query)).fetchall()

    async def get_by_id(self, id: int, table: SQLModel):
        return await self.__get(select(table).get(id))


class ConversationGetter(Getter):

    async def get_by_id(self, id: int):
        return await self.get_dy_id(id, ConversationModel)
    
    async def get_by_user(self, user: User):
        query = select(ConversationModel).where(ConversationModel.user_id == user.id)
        return await self.__get(query)


class UserGetter(Getter):

    async def get_by_id(self, id: int):
        return await self.get_dy_id(id, User)
    
    async def get_by_username(self, username: str):
        query = select(User).where(User.username == username)
        return await self.__get(query)
    
class MessageGetter(Getter):

    async def get_by_id(self, id: int):
        return await self.get_dy_id(id, Message)    

    async def get_by_user(self, user: User):
        query = select(Message).where(Message.user_id == user.id)
        return await self.__get(query)
    
    async def get_by_conversation(self, conversation: ConversationModel):
        query = select(Message).where(Message.conversation_id == conversation.id).order_by(Message.date)
        return await self.__get(query)


