from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)

from uuid import uuid4

from app.core.config import settings



client = QdrantClient(
    host=settings.QDRANT_HOST,
    port=settings.QDRANT_PORT
)


COLLECTION_NAME = "document_chunks"



def create_collection():

    collections = client.get_collections()

    exists = any(
        c.name == COLLECTION_NAME
        for c in collections.collections
    )


    if not exists:

        client.create_collection(
            collection_name=COLLECTION_NAME,

            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )



def insert_chunks(
    vectors,
    chunks,
    document_id,
    user_id,
    filename
):

    points = []


    for idx, (vector, text) in enumerate(
        zip(vectors, chunks)
    ):

        points.append(
    PointStruct(
        id=str(uuid4()),
        vector=vector,
        payload={
            "text": chunks,
            "document_id": document_id,
            "user_id": user_id,
            "filename": filename
        }
    )
)


    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )