from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def create_embedding(text: str):

    vector = model.encode(
        text
    )

    return vector.tolist()



def create_embeddings(chunks: list[str]):

    vectors = model.encode(
        chunks
    )

    return vectors.tolist()