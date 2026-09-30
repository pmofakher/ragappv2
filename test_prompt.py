from app.services.retriever import search_similar_chunks
from app.services.context_manager import build_context
from app.services.prompt import build_prompt


question = "What is machine learning?"

results = search_similar_chunks(
    query=question,
    user_id=1,
    limit=5
)

context = build_context(results)

prompt = build_prompt(
    question=question,
    context=context
)

print(prompt)