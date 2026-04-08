from langchain_ollama.llms import OllamaLLM
from backend.app.config.settings import settings

llm = OllamaLLM(model=settings.LLM_MODEL)

def generate_answer(context, question):
    prompt = f"""
    You are a helpful assistant.
    Answer based only on context
    if you don't know the answer, just say "I don't know"

    Context:
    {context}

    Question:
    {question}
    """

    return llm.invoke(prompt)