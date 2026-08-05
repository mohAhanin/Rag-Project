# Rag-Project

This is a simple Retrieval-Augmented Generation (RAG) project I built. It takes a small set of text documents, converts them into embeddings using the sentence-transformers library, and stores them in a ChromaDB vector database. When a question is asked, the project retrieves the most relevant pieces of text from the database and sends them along with the question to a free LLM API, which then generates an answer based only on that retrieved information. The dataset used here is a small set of made-up facts about a fictional bike company, just to keep things simple while testing the pipeline. This project was mainly built to understand the core RAG workflow: embed, store, retrieve, and generate.
"" 
"# Updated by mohAhanin" 
