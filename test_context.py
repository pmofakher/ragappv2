from app.services.retriever import search_similar_chunks
from app.services.context_manager import build_context


results = search_similar_chunks(
    query="What is machine learning?",
    user_id=1,
    limit=5
)

context = build_context(results)

print(context)