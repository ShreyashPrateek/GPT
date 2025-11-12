"""
utils.py — Helper functions for logging and data processing
"""

import os
from datetime import datetime

LOG_FILE = "logs/chat_logs.txt"

def log_message(user_input, response):
    """
    Append each interaction to a chat log file.
    """
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
        f.write(f"User: {user_input}\n")
        f.write(f"AI: {response}\n\n")

def clean_text(text):
    """
    Basic text cleaner to normalize whitespace.
    """
    return " ".join(text.strip().split())

def print_banner():
    print("=" * 60)
    print("🧠 Custom GPT — Powered by LangChain + Hugging Face")
    print("=" * 60)
