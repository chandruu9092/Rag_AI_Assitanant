from backend.app.db.vector_store import query_vector_store
from backend.app.services.llm_service import generate_answer

def ask_question(question: str):
    docs = query_vector_store(question)
    print(docs)
    context = "\n".join([doc.page_content for doc in docs])
    return generate_answer(context, question)




