from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import User


async def get_user_from_db(username: str, password: str, session: AsyncSession):
    query = select(User).where(User.username == username)\
                                       .where(User.password == password)
    return (await session.execute(query)).first()
