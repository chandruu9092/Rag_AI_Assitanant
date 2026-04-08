from fastapi import APIRouter
from backend.app.services.rag_service import ask_question

router = APIRouter()

@router.get("/ask")
def ask(question: str):
    answer = ask_question(question)
    return {"answer": answer}