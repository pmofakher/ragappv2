from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Document
from app.services.vector_db import delete_document_chunks


async def get_user_documents(
    db: AsyncSession,
    user_id: int
):
    result = await db.execute(
        select(Document)
        .where(Document.user_id == user_id)
        .order_by(Document.id.desc())
    )

    return result.scalars().all()


async def get_user_document(
    db: AsyncSession,
    document_id: int,
    user_id: int
):
    result = await db.execute(
        select(Document)
        .where(
            Document.id == document_id,
            Document.user_id == user_id
        )
    )

    return result.scalar_one_or_none()


async def delete_document(
    db: AsyncSession,
    document: Document
):
    await delete_document_chunks(document.id)

    await db.delete(document)
    await db.commit()