from fastapi import APIRouter
from app.services.retriever import search_similar_chunks


router = APIRouter()


@router.get("/search")
def search(q: str):

    results = search_similar_chunks(q)

    return {
        "query": q,
        "results": results
    }