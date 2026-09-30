from pydantic import BaseModel, Field


class RAGRequest(BaseModel):

    question: str = Field(
        min_length=1,
        max_length=2000
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20
    )

    score_threshold: float = Field(
        default=0.3,
        ge=0.0,
        le=1.0
    )


class RAGResponse(BaseModel):

    answer: str
    sources: list[dict]
    cached: bool = False