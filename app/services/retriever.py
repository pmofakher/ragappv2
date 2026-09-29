from app.services.embedding import create_embeddings
from app.services.vector_db import client, COLLECTION_NAME

from qdrant_client.models import Filter, FieldCondition, MatchValue

def search_similar_chunks(
    query: str,
    user_id: int,
    limit: int = 5
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


    chunks = []


    return [
        {
            "score": item.score,
            "text": item.payload["text"],
            "filename": item.payload["filename"]
        }
        for item in results
    ]