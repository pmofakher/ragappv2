from app.services.embedding import create_embeddings
from app.services.vector_db import client, COLLECTION_NAME

from qdrant_client.models import Filter, FieldCondition, MatchValue

def search_similar_chunks(
    query: str,
    user_id: int,
    limit: int = 5,
    score_threshold: float = 0.0
):

    # 1. query embedding
    vector = create_embeddings([query])[0]


    # 2. qdrant search
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        query_filter=Filter(
            must=[
                FieldCondition(
                    key="user_id",
                    match=MatchValue(
                        value=user_id
                    )
                )
            ]
        ),
        limit=limit
    )


    return [
        {
            "score": item.score,
            "text": item.payload.get("text", ""),
            "document_id": item.payload.get("document_id"),
            "filename": item.payload.get("filename"),
            "chunk_index": item.payload.get("chunk_index"),
        }
        for item in results
        if item.score >= score_threshold
    ]