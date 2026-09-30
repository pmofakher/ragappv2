from app.services.retriever import search_similar_chunks
from app.services.context_manager import build_context
from app.services.prompt import build_prompt
from app.services.llm import ask_llm
from app.services.cache import (
    make_cache_key,
    get_cache,
    set_cache,
)

import asyncio

MIN_TOP_K = 1
MAX_TOP_K = 20


def clamp_top_k(top_k: int) -> int:
    if top_k < MIN_TOP_K:
        return MIN_TOP_K
    if top_k > MAX_TOP_K:
        return MAX_TOP_K
    return top_k


async def generate_rag_answer(
    question: str,
    user_id: int,
    top_k: int = 5,
    score_threshold: float = 0.3,
):

    top_k = clamp_top_k(top_k)

    # -------------------------
    # 1. Cache
    # -------------------------

    cache_key = make_cache_key(
        user_id=user_id,
        question=question,
        top_k=top_k,
        score_threshold=score_threshold,
    )

    cached_result = await get_cache(cache_key)

    if cached_result is not None:

        cached_result["cached"] = True

        return cached_result


    # -------------------------
    # 2. Retrieval
    # -------------------------

    results = await asyncio.to_thread(
        search_similar_chunks,
        query=question,
        user_id=user_id,
        limit=top_k,
        score_threshold=score_threshold,
    )


    # -------------------------
    # 3. Context
    # -------------------------

    context = build_context(results)


    # -------------------------
    # 4. Prompt
    # -------------------------

    prompt = build_prompt(
        question=question,
        context=context,
    )


    # -------------------------
    # 5. LLM
    # -------------------------

    answer = await ask_llm(prompt)


    # -------------------------
    # 6. Response
    # -------------------------

    result = {
        "answer": answer,
        "sources": [
            {
                "document_id": chunk["document_id"],
                "filename": chunk["filename"],
                "chunk_index": chunk["chunk_index"],
                "score": chunk["score"],
            }
            for chunk in results
        ],
        "cached": False,
    }


    # -------------------------
    # 7. Save Cache
    # -------------------------

    await set_cache(
        cache_key,
        result,
    )


    return result