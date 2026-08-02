---
title: "RAG — Retrieval Augmented Generation"
difficulty: "hard"
labels: ["week-2", "rag", "embeddings"]
---

## Task Description
Build a basic RAG pipeline to answer questions from a document.

## Requirements
- Use LangChain or plain Python
- Load a PDF or text file (e.g., your resume or a Wikipedia article)
- Split into chunks, generate embeddings (OpenAI or free: sentence-transformers)
- Store in a vector store (ChromaDB or FAISS)
- Ask questions about the document — retrieve top-k chunks and generate answer

## Acceptance Criteria
- [ ] RAG pipeline working
- [ ] Can answer 5 sample questions from the document
- [ ] PR submitted
