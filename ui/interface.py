import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.llm_chain import get_response
from app.memory_manager import memory
from app.config import APP_NAME

st.set_page_config(page_title=f"{APP_NAME}", page_icon="🤖", layout="wide")

st.title(f"🤖 {APP_NAME}")
st.write("**Powered by LangChain + Hugging Face**")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your personal GPT. How can I help you today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_response(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.header("Options")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        memory.clear()
        st.rerun()
