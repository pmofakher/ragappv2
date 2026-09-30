import json

import redis.asyncio as redis

from app.core.config import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True,
)


CACHE_TTL = 3600


def make_cache_key(
    user_id: int,
    question: str,
    top_k: int,
    score_threshold: float,
):
    normalized_question = question.strip().lower()

    return (
        f"rag:"
        f"user:{user_id}:"
        f"q:{normalized_question}:"
        f"k:{top_k}:"
        f"s:{score_threshold}"
    )


async def get_cache(key: str):

    value = await redis_client.get(key)

    if value is None:
        return None

    return json.loads(value)


async def set_cache(
    key: str,
    value: dict,
    ttl: int = CACHE_TTL,
):

    await redis_client.set(
        key,
        json.dumps(value),
        ex=ttl,
    )