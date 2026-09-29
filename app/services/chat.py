from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.chat import ChatMessage


async def save_message(
    db: AsyncSession,
    user_id: int,
    role: str,
    content: str
):

    message = ChatMessage(
        user_id=user_id,
        role=role,
        content=content
    )

    db.add(message)

    await db.commit()


async def get_history(
    db: AsyncSession,
    user_id: int
):

    result = await db.execute(
        select(ChatMessage)
        .where(
            ChatMessage.user_id == user_id
        )
        .order_by(ChatMessage.id)
    )

    return result.scalars().all()