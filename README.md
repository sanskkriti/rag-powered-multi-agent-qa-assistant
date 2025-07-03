# 🧠 RAG-Powered Multi-Agent Q&A Assistant

A modular Streamlit-based question-answering app that routes user queries through different agents — including document-based retrieval (RAG), calculator, and dictionary responders.

---

## 🔍 Overview

This assistant demonstrates the architecture of a Retrieval-Augmented Generation (RAG) pipeline, integrated with a multi-agent query classifier. Although this version does **not use an LLM** for generation, it performs semantic search using `SentenceTransformers` and simulates tool routing (math/dictionary) like LangChain agents.

---

## ⚙️ Features

- 📄 **Document Retrieval**: Uses SentenceTransformer embeddings + cosine similarity for semantic search.
- 🔁 **Multi-Agent Routing**: Classifies queries and routes to appropriate tools:
  - `Calculator Tool` : Performs basic math if the query includes words like calculate, math, or solve.
  - `Dictionary` for known definitions
  - `RAG` for context-based retrieval from uploaded `.txt` documents
- 🧪 **Modular Structure**: Easily extendable to plug in LLMs (OpenAI, Hugging Face, etc.).
- 🖥️ **Frontend**: Built with Streamlit for interactive use.




