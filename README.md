# 🌟 LangChain + Ollama Series: Building Chatbots, APIs & RAG Pipelines

This repository is a personal learning journey exploring the power of **LangChain** and **open-source LLMs via Ollama**. Each project demonstrates a different real-world use case—from basic prompt interactions to FastAPI integrations and full Retrieval-Augmented Generation (RAG) pipelines.

---

## 📁 Project Structure


---

## 📦 Project 1: Search Box Chatbot (Customer Support Style)

**Summary:**  
A basic chatbot built using LangChain and Ollama where the user enters a query, and the LLM responds as a simulated customer support agent.

**Highlights:**
- PromptTemplate with role-based instructions
- User input handled via a search box
- LLM response streamed back for realistic interaction

---

## ⚡ Project 2: FastAPI + Ollama for Essay & Poem Generation

**Summary:**  
A FastAPI application that generates **essays or poems** based on the topic provided by the user.

**Endpoints:**
- `POST /essay` → Returns an essay on the given topic
- `POST /poem` → Returns a poem on the given topic

**Technologies:**
- LangChain + Ollama
- FastAPI
- JSON-based I/O for easy frontend or tool integration

---

## 🔍 Project 3: Retrieval-Augmented Generation (RAG) Pipeline

**Summary:**  
An end-to-end pipeline using LangChain to implement Retrieval-Augmented Generation with Ollama.

**Pipeline Flow:**
1. **Load** → Ingest documents
2. **Transform** → Chunk and clean text
3. **Embed** → Generate embeddings
4. **Store** → Save to a VectorDB (e.g., FAISS or Chroma)
5. **Query** → Accept user question
6. **Retrieve** → Fetch relevant documents
7. **Generate** → Use Ollama to respond with context

**Key Concepts:**
- LangChain Document Loaders, Text Splitters
- Embedding and Vector Stores
- Semantic Search + Context-Aware Generation

---

## 🛠️ Setup Instructions

### Prerequisites:
- Python 3.9+
- [Ollama installed](https://ollama.com/)
- Recommended models: `llama3`, `mistral`, etc.

### Install Dependencies:
Navigate to each folder and run:
```bash
pip install -r requirements.txt
```

### 🙌 Why This Series?

This repo helps solidify concepts around:

- LangChain workflows and modules  
- Prompt engineering  
- API-based LLM services  
- Building scalable RAG systems using **open-source LLMs** (no paid APIs!)  

---

## 🚀 Future Additions

- Frontend integration with Streamlit or Next.js  
- File/document upload support for RAG  
- Chat history & memory in chatbot  
- Evaluation of LLM outputs using LangChain tools  

---

## 📬 Feedback

Feel free to open issues or discussions if you're on a similar journey or have suggestions!

