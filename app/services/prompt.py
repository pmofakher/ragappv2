def build_prompt(question, context):

    prompt = f"""
You are a helpful AI assistant.

Answer only based on the provided context.

If the answer is not in the context,
say you don't know.

Context:
----------------
{context}
----------------

Question:
{question}

Answer:
"""

    return prompt