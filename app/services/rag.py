from app.services.retriever import search_similar_chunks
from app.services.context_manager import build_context
from app.services.prompt import build_prompt
from app.services.llm import ask_llm

DEFAULT_TOP_K = 5
MIN_TOP_K = 1
MAX_TOP_K = 50


def clamp_top_k(top_k: int) -> int:
    if top_k < MIN_TOP_K:
        return MIN_TOP_K
    if top_k > MAX_TOP_K:
        return MAX_TOP_K
    return top_k


async def generate_rag_answer(
    question: str,
    user_id: int,
    top_k: int = DEFAULT_TOP_K,
    score_threshold: float = 0.3,
):

    top_k = clamp_top_k(top_k)

    # 1. Retrieval
    results = search_similar_chunks(
        query=question,
        user_id=user_id,
        limit=top_k,
    )

    # 2. Context
    context = build_context(results)

    # 3. Prompt
    prompt = build_prompt(
        question=question,
        context=context,
    )

    # 4. LLM
    answer = ask_llm(prompt)

    return {
        "answer": answer,
        "sources": [
            {
                "document_id": point.payload["document_id"],
                "filename": point.payload["filename"],
                "chunk_index": point.payload["chunk_index"],
                "score": point.score,
            }
            for point in results
        ],
    }