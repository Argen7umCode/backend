from sqlalchemy.future import select
from models.models import User, ConversationModel, Message
from db import SessionMixin

from sqlmodel import SQLModel


class Getter(SessionMixin):

    async def get(self, query):
        session = await self.get_session().__anext__()
        return (await session.execute(query)).fetchall()

    async def get_by_id(self, id: int, table: SQLModel):
        return await self.get(select(table).get(id))

class ConversationGetter(Getter):

    async def get_by_id(self, id: int):
        return await self.get_dy_id(id, ConversationModel)
    
    async def get_by_user(self, user: User):
        query = select(ConversationModel).where(ConversationModel.user_id == user.id)
        return await self.get(query)

class UserGetter(Getter):

    async def get_by_id(self, id: int):
        return await self.get_dy_id(id, User)
    
    async def get_by_username(self, username: str):
        print(dir(self))
        query = select(User).where(User.username == username)
        return await self.get(query)
    
class MessageGetter(Getter):

    async def get_by_id(self, id: int):
        return await self.get_dy_id(id, Message)    

    async def get_by_user(self, user: User):
        query = select(Message).where(Message.user_id == user.id)
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

