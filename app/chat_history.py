from datetime import datetime
from typing import List, Dict
import streamlit as st

def init_chat_history():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "image_history" not in st.session_state:
        st.session_state.image_history = []
    if "last_chat_count" not in st.session_state:
        st.session_state.last_chat_count = 0
    if "last_image_count" not in st.session_state:
        st.session_state.last_image_count = 0

def auto_save_chat(messages: List[Dict]):
    current_count = len(messages)
    if current_count > st.session_state.last_chat_count and current_count > 1:
        # Get first user message as name
        name = "New Chat"
        for msg in messages:
            if msg.get("role") == "user":
                name = msg.get("content", "New Chat")[:30]
                break
        
        # Check if already saved
        existing = [h for h in st.session_state.chat_history if h.get("messages") == messages]
        if not existing:
            st.session_state.chat_history.append({
                "name": name,
                "type": "text",
                "messages": messages.copy()
            })
    st.session_state.last_chat_count = current_count

def auto_save_images(image_messages: List[Dict]):
    current_count = len(image_messages)
    if current_count > st.session_state.last_image_count:
        # Get last prompt as name
        name = image_messages[-1].get("prompt", "New Image")[:30]
        
        st.session_state.image_history.append({
            "name": name,
            "type": "image",
            "images": image_messages.copy()
        })
    st.session_state.last_image_count = current_count

def get_all_history() -> List[Dict]:
    all_history = st.session_state.get("chat_history", []) + st.session_state.get("image_history", [])
    return list(reversed(all_history))

def load_history_item(item: Dict):
    item_type = item.get("type", "text")  # Default to text for old items
    if item_type == "text":
        st.session_state.messages = item.get("messages", [])
        st.session_state.active_tab = 0
    elif item_type == "image":
        st.session_state.image_messages = item.get("images", [])
        st.session_state.active_tab = 1

def delete_history_item(item: Dict):
    item_type = item.get("type", "text")  # Default to text for old items
    if item_type == "text" and item in st.session_state.chat_history:
        st.session_state.chat_history.remove(item)
    elif item_type == "image" and item in st.session_state.image_history:
        st.session_state.image_history.remove(item)
