from sqlalchemy.future import select
from models.models import User, ConversationModel, Message
from db import SessionMixin

from sqlmodel import SQLModel


class Getter(SessionMixin):

    async def get(self, query):
        async with self.get_session() as session:
            return [item[0] for item in (await session.execute(query)).fetchall()] 

    async def get_by_id_(self, id: int, table: SQLModel):
        return await self.get(select(table).where(id == table.id))

class ConversationGetter(Getter):

    async def get_by_id(self, id: int):
        return (await self.get_by_id_(id, ConversationModel))[::-1]
    
    async def get_by_user(self, user: User):
        query = select(ConversationModel).join(Message).join(User).where(User == user)
        return (await self.get(query))[::-1]

class UserGetter(Getter):

    async def get_by_id(self, id: int):
        return await self.get_by_id_(id, User)
    
    async def get_by_username(self, username: str):
        query = select(User).where(User.username == username)
        return await self.get(query)
    
class MessageGetter(Getter):

    async def get_by_id(self, id: int):
        return await self.get_by_id_(id, Message)

    async def get_by_user(self, user: User):
        query = select(Message).where(Message.user_id == user.id)\
                               .order_by(Message.date)
        return await self.get(query)
    
    async def get_by_conversation(self, conversation: ConversationModel):
        query = select(Message).where(Message.conversation_id == conversation.id)\
                               .order_by(Message.date)
        return await self.get(query)

    async def get_by_user_and_id(self, user: User, id: int):
        query = select(Message).where(Message.id == id)\
                               .where(Message.user_id == user.id)\
                               .order_by(Message.date)
        return await self.get(query)
