# 🧠 Adaptive RAG System (Corrective → Self → Adaptive Evolution)

An advanced Retrieval-Augmented Generation (RAG) system that evolves through three architectural stages:

- Corrective RAG (v1.0.0)
- Self-RAG (v1.1.0)
- Adaptive RAG (v1.2.0)

This project demonstrates the progression from a basic RAG pipeline to a fully **dynamic, self-correcting, and routing-aware AI system**.

---

# 🚀 Project Overview

This system is designed to explore modern RAG architectures by implementing:

- Retrieval augmentation
- Self-evaluation loops
- Hallucination detection
- Answer quality grading
- Dynamic query routing

The final system behaves as an **adaptive reasoning pipeline** capable of selecting information sources, validating outputs, and correcting itself during inference.

---

# 🧬 System Evolution

## 🟢 v1.0.0 — Corrective RAG
- Basic retrieval-augmented generation
- Document grading before generation
- Simple corrective logic using web fallback

---

## 🟡 v1.1.0 — Self-RAG
Introduced self-evaluation mechanisms:

- Hallucination detection (fact grounding check)
- Answer relevance grading
- Iterative correction loops
- Web search fallback for low-quality responses

---

## 🔵 v1.2.0 — Adaptive RAG (Current)
Major architectural upgrade introducing:

### ✨ Key Features
- Intelligent query routing (vectorstore vs web search)
- Pre-retrieval decision making
- Structured LLM router using Pydantic
- Dynamic multi-source retrieval system
- Self-correcting generation loop (from v1.1.0)

---

# 🏗️ Architecture

The system operates as a multi-stage decision graph:

### 1. Query Routing
Routes user input to:
- Internal vector database
- External web search

### 2. Retrieval
Fetches relevant documents based on routing decision

### 3. Document Grading
Filters irrelevant context

### 4. Generation
Produces initial response using LLM

### 5. Self-Evaluation (v1.1.0 feature)
- Hallucination detection
- Answer relevance grading

### 6. Conditional Correction
- Regenerate if hallucinated
- Web search fallback if irrelevant
- Return final answer if valid

---

# ⚙️ Tech Stack

- Python
- LangChain
- LangGraph
- OpenAI GPT-4.1-mini
- Pydantic (structured outputs)
- ChromaDB / Vector Store
- Prompt Engineering

---

# 🔄 Key Capabilities

- Retrieval-Augmented Generation (RAG)
- Self-correcting reasoning loops
- Multi-source adaptive retrieval
- Hallucination detection
- Answer quality validation
- Dynamic routing between knowledge sources

---

# 📊 Why This Project Matters

This project demonstrates:

- Advanced RAG system design
- Agentic AI architecture thinking
- Multi-step reasoning pipelines
- LLM-based decision systems
- Production-style LangGraph workflows

---

# 🧪 How It Works (Simplified Flow)

User Query  
→ Routing (Vectorstore / Web)  
→ Retrieval  
→ Document Grading  
→ Generation  
→ Hallucination Check  
→ Answer Evaluation  
→ Final Response / Retry Loop  

---

# 📌 Future Improvements

- Memory-based conversational RAG
- Multi-agent collaboration system
- Evaluation dashboard (accuracy metrics)
- API + frontend deployment
- Streaming responses UI

---

# 🏁 Summary

This project demonstrates the evolution of RAG systems:

- From static retrieval (Corrective RAG)
- To self-evaluating pipelines (Self-RAG)
- To intelligent routing systems (Adaptive RAG)

It showcases a full progression toward **agentic, adaptive AI architectures**.
