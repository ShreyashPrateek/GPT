"""
main.py — Entry point for LangChain + Hugging Face GPT App
"""

import os
from dotenv import load_dotenv
from app.llm_chain import get_response
from app.memory_manager import memory
from app.retriever import load_vectorstore, get_context
from app.utils import log_message

# ------------------ LOAD ENVIRONMENT VARIABLES ------------------
load_dotenv()

print("🚀 Starting LangChain + Hugging Face GPT...")

# Optional knowledge base initialization
try:
    vectorstore = load_vectorstore()
    print("✅ Knowledge base loaded successfully.")
except Exception as e:
    print("⚠️ No knowledge base found or failed to load:", e)
    vectorstore = None

# ------------------ MAIN CHAT LOOP (CLI VERSION) ------------------
if __name__ == "__main__":
    print("\n🤖 Custom GPT is ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        # If retriever exists, include context
        context = ""
        if vectorstore:
            context = get_context(vectorstore, user_input)

        response = get_response(user_input, context)
        print("AI:", response)

        # Save chat to logs
        log_message(user_input, response)
