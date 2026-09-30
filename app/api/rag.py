from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user
from app.models.user import User

from app.schemas.rag import (
    RAGRequest,
    RAGResponse,
)

from app.services.rag import generate_rag_answer


router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)


@router.post(
    "/ask",
    response_model=RAGResponse
)
async def ask(
    data: RAGRequest,
    current_user: User = Depends(get_current_user),
):

    result = await generate_rag_answer(
        question=data.question,
        user_id=current_user.id,
        top_k=data.top_k,
        score_threshold=data.score_threshold,
    )

    return result