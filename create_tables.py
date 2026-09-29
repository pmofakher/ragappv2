import asyncio

from app.database.session import engine
from app.database.base import Base

from app.models import *
from app.models.chat import ChatMessage

async def main():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )


asyncio.run(main())