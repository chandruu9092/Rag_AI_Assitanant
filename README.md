# AI Assistant - RAG-powered PDF Question Answering

A Retrieval-Augmented Generation (RAG) system that lets you upload PDF documents and ask questions about their content. Built with FastAPI, LangChain, FAISS, and Ollama for fully local, private inference.

## How It Works

```
Upload Phase:  PDF → Extract Text (PyMuPDF) → Chunk → Embed (Ollama) → Store in FAISS
Query Phase:   Question → Embed → Search FAISS (top 3) → LLM generates answer from context
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Web Framework | FastAPI + Uvicorn |
| LLM | Ollama (llama3.2:3b by default) |
| Embeddings | LangChain Ollama |
| Vector Store | FAISS (CPU) |
| PDF Parsing | PyMuPDF (fitz) |
| Orchestration | LangChain |
| Containerization | Docker Compose |

## Project Structure

```
ai-assistant/
├── backend/
│   ├── app/
│   │   ├── main.py                   # FastAPI app entrypoint
│   │   ├── config/
│   │   │   └── settings.py           # Environment-based configuration
│   │   ├── db/
│   │   │   └── vector_store.py       # FAISS index creation and querying
│   │   ├── routes/
│   │   │   ├── upload.py             # POST /upload - PDF ingestion
│   │   │   └── query.py              # GET /ask - Question answering
│   │   ├── services/
│   │   │   ├── embedding_service.py  # Ollama embedding generation
│   │   │   ├── llm_service.py        # LLM prompt and response handling
│   │   │   └── rag_service.py        # RAG pipeline orchestration
│   │   └── utils/
│   │       ├── pdf_loader.py         # PDF text extraction
│   │       └── chunking.py           # Text chunking with overlap
│   ├── data/
│   │   └── faiss_index/              # Persisted vector index
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
├── frontend/                         # Frontend (coming soon)
├── docker-compose.yml
└── README.md
```

## Prerequisites

- **Python 3.10+**
- **Ollama** installed and running locally ([ollama.com](https://ollama.com))
- An Ollama model pulled (default: `llama3.2:3b`)

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd ai-assistant
   ```

2. **Create and activate a virtual environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` to set your preferred Ollama model:
   ```
   LLM_MODEL='llama3.2:3b'
   ```

5. **Pull the Ollama model**
   ```bash
   ollama pull llama3.2:3b
   ```

## Running

Start the Ollama server (if not already running):
```bash
ollama serve
```

Start the FastAPI application:
```bash
cd backend
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

## API Endpoints

### Upload a PDF

```bash
curl -X POST http://localhost:8000/upload \
  -F "file=@/path/to/document.pdf"
```

**Response:**
```json
{"message": "File processed successfully"}
```

### Ask a Question

```bash
curl "http://localhost:8000/ask?question=What%20is%20this%20document%20about"
```

**Response:**
```json
{"answer": "Based on the document..."}
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_MODEL` | `llama3` | Ollama model name for embeddings and generation |

Chunking defaults (in `backend/app/utils/chunking.py`):
- **Chunk size:** 500 characters
- **Overlap:** 100 characters

Vector search returns the top **3** most relevant chunks per query.

## License

This project is for personal learning and experimentation.
