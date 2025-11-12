"""
prompt_templates.py — Defines system and user prompt templates
"""

from langchain_core.prompts import PromptTemplate

# ------------------ DEFAULT CHAT TEMPLATE ------------------
default_template = """
You are a helpful AI assistant trained to provide accurate, concise, and friendly responses.

Conversation so far:
{history}

User: {user_input}
Assistant:
"""

chat_prompt = PromptTemplate(
    input_variables=["history", "user_input"],
    template=default_template,
)

# ------------------ RAG / KNOWLEDGE-BASED TEMPLATE ------------------
rag_template = """
You are a knowledgeable assistant that answers user queries using the given context.

Context:
{context}

Conversation so far:
{history}

User: {user_input}
Assistant:
"""

rag_prompt = PromptTemplate(
    input_variables=["history", "context", "user_input"],
    template=rag_template,
)
