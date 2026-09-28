from fastapi import FastAPI

from app.api.auth import router as auth_router


app = FastAPI(
    title="RAG Docker 2"
)


app.include_router(auth_router)


@app.get("/")
async def root():
    return {
        "message": "RAG Docker 2 is running"
    }