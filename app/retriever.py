"""
retriever.py — Handles knowledge base retrieval using Chroma or FAISS
"""

import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# ------------------ CONFIG ------------------
CHROMA_PATH = "data/embeddings"

def load_vectorstore():
    """
    Loads a Chroma vector store from disk if available.
    """
    if not os.path.exists(CHROMA_PATH):
        raise FileNotFoundError(f"Vector store not found at {CHROMA_PATH}")
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    return vectorstore


def get_context(vectorstore, query, k=3):
    """
    Retrieves top-k relevant chunks for a given user query.
    Returns combined context as a string.
    """
    docs = vectorstore.similarity_search(query, k=k)
    context = "\n".join([doc.page_content for doc in docs])
    return context
