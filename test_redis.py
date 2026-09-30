import asyncio

from app.services.cache import (
    redis_client,
    set_cache,
    get_cache,
)


async def main():

    key = "test:key"

    await set_cache(
        key,
        {
            "message": "Redis works"
        }
    )

    result = await get_cache(key)

    print(result)

    await redis_client.close()


asyncio.run(main())