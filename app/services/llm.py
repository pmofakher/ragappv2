from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    api_key=settings.LLM_API_KEY,
    base_url=settings.LLM_API_BASE
)



def ask_llm(prompt: str):

    response = client.chat.completions.create(

        model=settings.LLM_MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content