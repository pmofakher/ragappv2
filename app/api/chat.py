from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.rag import answer_question
from app.services.chat import save_message
from app.database.session import get_db
from app.core.dependencies import get_current_user


router = APIRouter()


@router.post("/chat")
async def chat(
    question: str,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):

    # save user message
    await save_message(
        db=db,
        user_id=current_user.id,
        role="user",
        content=question
    )


    # RAG + LLM
    result = answer_question(question,current_user.id)


    # save assistant answer
    await save_message(
        db=db,
        user_id=current_user.id,
        role="assistant",
        content=result["answer"]
    )


    return {
        "answer": result["answer"],
        "sources": result["sources"]
    }