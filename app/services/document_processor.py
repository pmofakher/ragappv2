from app.utils.pdf import extract_text
from app.services.chunker import split_text
from app.services.embedding import create_embeddings
from app.services.vector_db import insert_chunks



async def process_document(
    filepath: str,
    document_id: int,
    user_id: int,
    filename: str
):

    # 1. Extract text
    text = extract_text(filepath)


    # 2. Chunking
    chunks = split_text(text)


    # 3. Embedding
    vectors = create_embeddings(chunks)


    # 4. Store in Qdrant
    insert_chunks(
        vectors=vectors,
        chunks=chunks,
        document_id=document_id,
        user_id=user_id,
        filename=filename
    )


    return {
        "chunks": len(chunks)
    }