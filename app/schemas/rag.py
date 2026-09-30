from pydantic import BaseModel


class RAGRequest(BaseModel):
    question: str
    top_k: int = 5
    score_threshold: float = 0.3


class RAGResponse(BaseModel):
    answer: str
    sources: list[dict]
    cached: bool = False