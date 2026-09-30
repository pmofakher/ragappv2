1. Project Setup
Project structure, FastAPI, configuration, and dependencies.

2. Docker
Running the entire system with Docker Compose.

3. PostgreSQL
Storing users, documents, metadata, and application data.

4. Redis
Caching, sessions, and temporary tasks.

5. JWT Auth
Registration, login, token handling, and API protection.

6. PDF Upload
PDF upload → file storage → document registration.

7. PDF Extraction
PDF → raw text.

8. Chunking + Embedding + Qdrant
Text → small chunks → embedding → storing vectors in Qdrant.

9. Vector Search ← Current Step
User query → embedding → search in Qdrant → retrieving the most relevant chunks.

10. RAG ← Next Step
Relevant chunks → context construction → sending to LLM → generating answer + sources.

11. Memory / History
Maintaining conversation state and enabling multi-turn queries.

12. Permissions
Ensuring users can only retrieve their own authorized documents and chunks.

13. Retrieval Quality
Improving search, similarity, filtering, reranking, and context quality.

14. Chat System
Sessions, conversations, messages, and a complete chat API.

15. Frontend
UI for uploads, document management, chat, and displaying sources.

16. Testing
Unit/API tests, validation, error handling, and edge cases.

17. Production
Security, logging, environment configuration, production Docker setup, deployment, and monitoring.
