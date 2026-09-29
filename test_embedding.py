from app.services.embedding import create_embedding


text = """
Machine learning is a subset of artificial intelligence.
"""


vector = create_embedding(text)


print(len(vector))
print(vector[:10])