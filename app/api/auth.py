from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse
)

from app.services.auth import (
    create_user,
    authenticate_user,
    UserAlreadyExistsError
)

from app.core.security import create_access_token

from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    status_code=201
)
async def register(
    data: RegisterRequest,
    db: AsyncSession = Depends(get_db)
):
    try:
        user = await create_user(
            db,
            data.username,
            data.email,
            data.password
        )
    except UserAlreadyExistsError as exc:
        raise HTTPException(
            status_code=409,
            detail=str(exc)
        )

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }


@router.post(
    "/login",
    response_model=TokenResponse
)
async def login(
    data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(
        db,
        data.username,
        data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(user.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }



@router.get("/me")
async def me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }
    