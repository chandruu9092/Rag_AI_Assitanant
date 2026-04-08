import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from backend.app.config.settings import settings

embedding = OllamaEmbeddings(model=settings.LLM_MODEL)

FAISS_INDEX_PATH = "data/faiss_index"

def create_vector_store(chunks):
    db = FAISS.from_texts(chunks, embedding)
    db.save_local(FAISS_INDEX_PATH)

def query_vector_store(query):
    db = FAISS.load_local(FAISS_INDEX_PATH, embedding, allow_dangerous_deserialization=True)
    if db is None:
        raise ValueError("No documents uploaded yet. Please upload a file first.")
    return db.similarity_search(query, k=3)

