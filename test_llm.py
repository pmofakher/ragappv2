from app.services.llm import ask_llm


answer = ask_llm(
    "Explain RAG in one sentence"
)


print(answer)