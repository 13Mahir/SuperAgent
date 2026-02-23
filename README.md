# 🤖 SuperAgent

SuperAgent is an advanced, flexible AI assistant platform. It pairs a **Next.js frontend** with a robust **FastAPI Python backend**, utilizing the power of Google's Gemini models (via LiteLLM) and Composio for extensive tool execution capabilities. It also includes built-in support for Retrieval-Augmented Generation (RAG) using ChromaDB and document ingestion.

---

## 🏗 Repository Structure

Since SuperAgent uses a decoupled architecture, this repository contains two primary workspaces:

- `frontend/` - The Next.js web application (React, TailwindCSS)
- `backend/` - The Python FastAPI backend (LiteLLM, LangChain, ChromaDB)

---

## 🚀 Quick Start Guide

### 1. Backend Setup

The backend handles the LLM logic, conversation history, RAG chunking, and tool execution. **Note: It requires Python 3.12.**

```bash
cd backend
```

**Create and activate a virtual environment:**
```bash
# Strongly recommended to use Python 3.12 
python3.12 -m venv .venv
source .venv/bin/activate
```

**Install requirements:**
```bash
pip install -r requirements.txt
```
*(The backend dependencies strictly require Pydantic v2 and compatible libraries.)*

**Configure Environment Variables:**
Copy the example environment file and fill in your keys:
```bash
cp .env.example .env
```
Ensure you provide a valid `LLM_API_KEY` (Defaults to Gemini 2.5 Flash API Key).

**Start the API Server:**
```bash
python main.py
```
*The backend runs on `http://localhost:5050`.*


### 2. Frontend Setup

The frontend is a chat interface that communicates with the API via REST and WebSockets.

```bash
cd frontend
```

**Install Node Dependencies:**
```bash
npm install
```

**Start the Development Server:**
```bash
npm run dev
```
*The frontend runs on `http://localhost:3000`.*

---

## 🛠 Key Technologies
- **Frontend**: Next.js (App Router), React, TailwindCSS, WebSockets
- **Backend**: Python 3.12, FastAPI, LiteLLM, LangChain, Composio
- **Vector DB**: ChromaDB

## 📡 Architecture Highlights
- **Interactive Tool Execution:** Configured via Composio to let the agent natively interact with APIs on your behalf.
- **RAG Readiness:** Built-in endpoints to ingest PDFs, split documents, and store them securely in ChromaDB for similarity searching.
- **WebSocket Streaming:** Instead of just REST, the chat heavily relies on WebSocket connections (`ws://localhost:5050/chat/ws`) to stream an LLM's thought process step-by-step to the UI.

---

## 🤝 Contribution
Contributions are welcome! If you're encountering library conflict issues (specifically regarding Pydantic/ChromaDB), please ensure that you are strictly utilizing **Python 3.12** in your virtual environment.
