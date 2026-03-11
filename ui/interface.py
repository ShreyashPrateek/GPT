import streamlit as st
import sys
import os
from io import BytesIO

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.llm_chain import get_response
from app.memory_manager import memory
from app.config import APP_NAME
from app.image_generator import generate_image
from app.chat_history import init_chat_history, auto_save_chat, auto_save_images, get_all_history, load_history_item, delete_history_item

st.set_page_config(page_title=f"{APP_NAME}", page_icon="🤖", layout="wide")

st.title(f"🤖 {APP_NAME}")
st.write("**Powered by LangChain + Hugging Face**")

init_chat_history()

if "active_tab" not in st.session_state:
    st.session_state.active_tab = 0

tab1, tab2 = st.tabs(["💬 Text Chat", "🎨 Image Generation"])

with tab1:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your personal GPT. How can I help you today?"}]
    
    auto_save_chat(st.session_state.messages)

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

with tab2:
    st.subheader("Generate Images from Text")
    
    if "image_messages" not in st.session_state:
        st.session_state.image_messages = []
    
    if st.session_state.image_messages:
        auto_save_images(st.session_state.image_messages)
    
    for msg in st.session_state.image_messages:
        st.write(f"**Prompt:** {msg['prompt']}")
        st.image(msg['image'], use_container_width=True)
        st.divider()
    
    image_prompt = st.text_area("Describe the image you want to generate:", height=100, placeholder="A serene landscape with mountains and a lake at sunset...")
    
    if st.button("🎨 Generate Image", type="primary"):
        if image_prompt:
            with st.spinner("Creating your image..."):
                image = generate_image(image_prompt)
                if image:
                    buf = BytesIO()
                    image.save(buf, format="PNG")
                    image_bytes = buf.getvalue()
                    
                    st.session_state.image_messages.append({
                        "prompt": image_prompt,
                        "image": image_bytes
                    })
                    
                    st.rerun()
                else:
                    st.error("Failed to generate image. Please try again.")
        else:
            st.warning("Please enter a description first.")

with st.sidebar:
    st.header("Options")
    
    if st.button("New Chat", use_container_width=True):
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your personal GPT. How can I help you today?"}]
        memory.clear()
        st.rerun()
    
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your personal GPT. How can I help you today?"}]
        if "image_messages" in st.session_state:
            st.session_state.image_messages = []
        memory.clear()
        st.rerun()
    
    st.divider()
    st.subheader("📜 History")
    
    history = get_all_history()
    if history:
        for idx, item in enumerate(history):
            icon = "💬" if item.get("type") == "text" else "🎨"
            
            if st.session_state.get(f"edit_{idx}"):
                new_name = st.text_input("Rename:", value=item['name'], key=f"rename_{idx}")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✔️ Save", key=f"save_{idx}", use_container_width=True):
                        item['name'] = new_name
                        st.session_state[f"edit_{idx}"] = False
                        st.rerun()
                with col2:
                    if st.button("❌ Cancel", key=f"cancel_{idx}", use_container_width=True):
                        st.session_state[f"edit_{idx}"] = False
                        st.rerun()
            else:
                col1, col2, col3 = st.columns([2.5, 0.75, 0.75])
                with col1:
                    if st.button(f"{icon} {item['name']}", key=f"load_{idx}", use_container_width=True):
                        load_history_item(item)
                        memory.clear()
                        st.rerun()
                with col2:
                    if st.button("✏️", key=f"edit_{idx}_btn"):
                        st.session_state[f"edit_{idx}"] = True
                        st.rerun()
                with col3:
                    if st.button("🗑️", key=f"del_{idx}"):
                        delete_history_item(item)
                        st.rerun()
    else:
        st.info("No saved history")
