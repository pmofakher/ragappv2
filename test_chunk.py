from app.services.chunker import split_text


text = """
Machine learning is a subset of artificial intelligence.
It allows computers to learn from data.

Deep learning is a branch of machine learning.
"""


chunks = split_text(text)


for i, chunk in enumerate(chunks):

    print(
        "\nCHUNK",
        i
    )

    print(chunk)