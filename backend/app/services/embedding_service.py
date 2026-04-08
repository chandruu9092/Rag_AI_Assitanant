from langchain_community.embeddings import OllamaEmbeddings
from backend.app.config.settings import settings

embedding_model = OllamaEmbeddings(model=settings.LLM_MODEL)

def get_embeddings(texts):
    return embedding_model.embed_documents(texts)