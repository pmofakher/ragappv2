from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.core.security import (
    hash_password,
    verify_password
)


class UserAlreadyExistsError(Exception):
    pass


async def create_user(
    db: AsyncSession,
    username: str,
    email: str,
    password: str
):
    user = User(
        username=username,
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()

        raise UserAlreadyExistsError(
            "Username or email is already registered"
        )

    await db.refresh(user)

    return user


async def authenticate_user(
    db: AsyncSession,
    username: str,
    password: str
):
    result = await db.execute(
        select(User).where(
            User.username == username
        )
    )

    user = result.scalar_one_or_none()

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    return user