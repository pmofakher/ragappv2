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

async def generate_rag_answer(
    question: str,
    user_id: int,
    top_k: int = 5,
    score_threshold: float = 0.3,
):

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
        top_k=top_k,
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
                "document_id": point.payload["document_id"],
                "filename": point.payload["filename"],
                "chunk_index": point.payload["chunk_index"],
                "score": point.score,
            }
            for point in results
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