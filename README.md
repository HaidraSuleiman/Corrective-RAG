# Corrective RAG (CRAG) with LangGraph, ChromaDB & Tavily

A Corrective Retrieval-Augmented Generation (CRAG) system built with LangGraph, Chroma vector database, OpenAI GPT-4.1-mini, and Tavily web search.

This project implements a RAG pipeline that evaluates retrieval quality and dynamically triggers web search when necessary.

---

# Overview

Traditional RAG systems directly use retrieved documents without validation.  
This project improves reliability by introducing a corrective feedback loop:

- Retrieved documents are graded for relevance using an LLM
- Irrelevant or insufficient context triggers web search fallback
- Final responses are generated using filtered and augmented context

---

# Architecture

## Workflow Diagram

![Graph Architecture](graph.png)

---

## Execution Flow

User Question  
→ Retrieve (Chroma Vector DB)  
→ Grade Documents (LLM-based relevance check)  
→ If relevant → Generate  
→ If irrelevant → Web Search → Generate  
→ Final Answer  

---

# Project Structure
corrective-rag/
│
├── main.py
├── ingestion.py
│
├── graph/
│ ├── graph.py
│ ├── state.py
│ ├── consts.py
│ │
│ ├── nodes/
│ │ ├── retrieve.py
│ │ ├── grade_documents.py
│ │ ├── web_search.py
│ │ └── generate.py
│ │
│ └── chains/
│ ├── generation.py
│ └── retrieval_grader.py
│
└── .chroma/


---

# Core Components

## Ingestion Pipeline (ingestion.py)

- Loads and processes documents
- Splits text into chunks
- Generates embeddings using OpenAI
- Stores vectors in ChromaDB
- Exposes retriever for semantic search

---

## Retrieval Node (retrieve.py)

- Accepts user question
- Queries vector database
- Returns top relevant documents

---

## Document Grading (retrieval_grader.py)

- Uses LLM to classify document relevance
- Output is binary:
  - yes → relevant
  - no → irrelevant

---

## Document Filtering (grade_documents.py)

- Iterates over retrieved documents
- Filters irrelevant content
- Sets flag for web search if needed

---

## Web Search Node (web_search.py)

- Uses Tavily API for live search
- Extracts top results
- Merges results into a single context document
- Appends to existing document set

---

## Generation Chain (generation.py)

- Uses GPT-4.1-mini
- Generates final answer
- Uses retrieved + web-augmented context
- Limited to 3 sentences

---

## State Definition (state.py)

Shared graph state:

```python
question: str
generation: str
web_search: bool
documents: list
```

# Features

Corrective RAG pipeline
LLM-based document relevance grading
Web search fallback mechanism
Vector database retrieval with ChromaDB
LangGraph state machine orchestration
Structured LLM outputs using Pydantic
Modular node-based architecture
# Tech Stack
LangChain
LangGraph
OpenAI GPT-4.1-mini
ChromaDB
Tavily API
Python
Pydantic
dotenv

# Setup Instructions
## 1. Clone repository
git clone <repo-url>
cd corrective-rag
## 2. Create virtual environment
python -m venv .venv

Activate:

Windows:
.venv\Scripts\activate
Mac/Linux:
source .venv/bin/activate
## 3. Install dependencies
pip install -r requirements.txt
## 4. Environment variables

Create a .env file:

OPENAI_API_KEY=your_key
TAVILY_API_KEY=your_key
## 5. Run project
python main.py
# Example Execution
Hello from corrective-rag!

---RETRIEVE---
---CHECKING DOCUMENT RELEVANCE---
---GENERATE---

Final answer returned from LLM


# This project demonstrates:

Self-correcting RAG systems
LLM-as-a-judge pattern for retrieval validation
Hybrid knowledge retrieval (vector DB + web search)
Graph-based AI workflow orchestration
Production-style modular AI system design

# Future Improvements
Add conversational memory
Improve retrieval ranking with rerankers
Add streaming responses
Build FastAPI or Streamlit UI
Add evaluation metrics (faithfulness, relevance scoring)
