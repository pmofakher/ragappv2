from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    api_key=settings.LLM_API_KEY,
    base_url=settings.LLM_API_BASE
)



async def ask_llm(prompt: str):

    response = await client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content