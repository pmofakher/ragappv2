SYSTEM_PROMPT = """
You are a helpful assistant.

Answer the user's question using ONLY the provided context.

Rules:
- Do not use information outside the context.
- If the answer is not available in the context, say:
  "I don't know based on the provided documents."
- Do not invent information.
"""


def build_prompt(
    question: str,
    context: str
):

    return f"""
{SYSTEM_PROMPT}

Context:
----------------
{context}
----------------

User Question:
{question}

Answer:
""".strip()