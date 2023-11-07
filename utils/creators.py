from db import SessionMixin
from typing import Any


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
