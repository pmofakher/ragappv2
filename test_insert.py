import asyncio

from app.database.session import async_session
from app.models.user import User


async def main():

    async with async_session() as session:

        user = User(
            username="pezhman",
            email="test@test.com",
            password_hash="hashed_password"
        )


        session.add(user)

        await session.commit()


asyncio.run(main())