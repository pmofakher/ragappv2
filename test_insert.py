import asyncio

from app.database.session import async_session
from app.models.user import User
from app.core.security import hash_password


async def main():

    async with async_session() as session:

        user = User(
            username="pezhman",
            email="test@test.com",
            password_hash=hash_password("password123")
        )


        session.add(user)

        await session.commit()


asyncio.run(main())