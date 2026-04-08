import os
from dotenv import load_dotenv

load_dotenv()  # ✅ Load only once here

class Settings:
    LLM_MODEL = os.getenv("LLM_MODEL", "llama3")

settings = Settings()