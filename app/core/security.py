from pwdlib import PasswordHash
from pwdlib.exceptions import UnknownHashError
from jose import jwt

from app.core.config import settings


password_hash = PasswordHash.recommended()

ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    password: str,
    hashed_password: str
) -> bool:
    try:
        return password_hash.verify(
            password,
            hashed_password
        )
    except UnknownHashError:
        return False


def create_access_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id)
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=ALGORITHM
    )


def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=[ALGORITHM]
    )