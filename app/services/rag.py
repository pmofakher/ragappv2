from app.services.retriever import search_similar_chunks
from app.services.prompt import build_prompt
from app.services.llm import ask_llm



def answer_question(question, user_id):

    chunks = search_similar_chunks(
        question,
        user_id,
        limit=5
    )


    context = "\n\n".join(
        [
            " ".join(chunk["text"]) if isinstance(chunk["text"], list) else chunk["text"]
            for chunk in chunks
        ]
    )


    prompt = build_prompt(
        question,
        context
    )


    answer = ask_llm(prompt)


    return {
        "answer": answer,
        "sources": [
            {
                "filename": c["filename"],
                "score": c["score"]
            }
            for c in chunks
        ]
    }