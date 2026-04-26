# 📚 Grounded Knowledge Engine (RAG System)

## 🚀 Overview

Grounded Knowledge Engine is a **Retrieval-Augmented Generation (RAG)** system that answers user queries based on custom documents.
It combines **document retrieval + LLM generation** to provide accurate, context-aware responses.

---

## 🎯 Features

* 🔍 Document ingestion (PDF support)
* ✂️ Intelligent text chunking
* 🧠 Embedding-based semantic search
* 📦 Vector database (Chroma)
* 🔎 Context retrieval (Top-K search / MMR)
* 🤖 LLM-based answer generation (Ollama)
* 🌐 FastAPI backend
* 🖥️ Streamlit UI
* ⚡ Optional streaming responses

---

## 🧱 Architecture

User Query → FastAPI → Retriever → Vector DB → Context
→ LLM (Ollama) → Generated Answer → UI

---

## 📂 Project Structure

```
grounded-knowledge-engine/
│
├── app/
│   ├── api/              # FastAPI server
│   ├── ingestion/        # Loader, chunking
│   ├── embeddings/       # Embedding model
│   ├── vectorstore/      # Chroma DB
│   ├── retrieval/        # Retriever logic
│   ├── generation/       # LLM + prompts
│   ├── pipeline/         # RAG pipeline
│   └── utils/            # Logging
│
├── data/
│   └── documents/        # Input PDFs
│
├── ui/
│   └── app.py            # Streamlit UI
│
├── evaluation/           # RAGAS evaluation
├── requirements.txt
└── README.md
```

---

## UI Preview

![alt text](<Screenshot 2026-04-26 221427.png>)


## ⚙️ Installation

### 1. Clone repository

```bash
git clone <repo-url>
cd grounded-knowledge-engine
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Setup LLM (Ollama)

Install Ollama and pull model:

```bash
ollama pull mistral
```

---

## ▶️ Running the Project

### 🔹 1. Start FastAPI backend

```bash
uvicorn app.api.server:app --reload
```

### 🔹 2. Open API docs

```
http://127.0.0.1:8000/docs
```

---

### 🔹 3. Start Streamlit UI

```bash
streamlit run ui/app.py
```

Open:

```
http://localhost:8501
```

---

## 🧪 Example Query

```
What is transformer architecture?
```

---

## 📊 Evaluation (RAGAS)

Run evaluation:

```bash
python evaluation/run_ragas.py
```

Metrics used:

* Faithfulness
* Answer Relevancy

---

## ⚡ Key Learnings

* Built a complete **end-to-end RAG pipeline**
* Understood **retrieval vs generation trade-offs**
* Implemented **streaming responses**
* Explored **evaluation using RAGAS**

---

## ⚠️ Limitations

* Slow response with local LLM (Ollama)
* Limited scalability
* Requires optimization for large datasets

---

## 🔮 Future Improvements

* Replace Ollama with **Gemini / OpenAI API**
* Add **Excel-based structured data (Light RAG)**
* Implement **tool calling / agentic workflows**
* Add **PDF report generation**
* Optimize retrieval (MMR, reranking)

---

## 👨‍💻 Author

**Hemanth Kumar Nunna**
AIML Student | AI/ML Enthusiast

---

## ⭐ Acknowledgements

* LangChain
* ChromaDB
* Ollama
* FastAPI
* Streamlit
* RAGAS

---
