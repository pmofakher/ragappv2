from fastapi import FastAPI


app = FastAPI(
    title="RAG Docker 2"
)


@app.get("/")
async def root():
    return {
        "message": "RAG Docker 2 is running"
    }