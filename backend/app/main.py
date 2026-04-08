from fastapi import FastAPI
from backend.app.routes import upload
from backend.app.routes import query

app = FastAPI()

app.include_router(upload.router)
app.include_router(query.router)