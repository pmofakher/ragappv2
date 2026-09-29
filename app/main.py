from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.documents import router as document_router
from app.api import search
from app.api import chat


app = FastAPI(
    title="RAG Docker 2"
)


app.include_router(auth_router)

app.include_router(document_router)

app.include_router(
    search.router,
    prefix="/api"
)

app.include_router(
    chat.router,
    prefix="/api"
)






@app.get("/")
async def root():
    return {
        "message": "RAG Docker 2 is running"
    }