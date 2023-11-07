from db import SessionMixin
from typing import Any


class Creator(SessionMixin):

    async def create(self, item: Any):
        async with self.get_session() as session:
            session.add(item)
            await session.commit()
        return item

class ConversationCreator(Creator):
    pass

class MessageCreator(Creator):
    pass

class UserCreator(Creator):
    pass
