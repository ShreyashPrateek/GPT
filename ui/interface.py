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

st.set_page_config(page_title=f"{APP_NAME}", page_icon="🤖", layout="wide")

st.title(f"🤖 {APP_NAME}")
st.write("**Powered by LangChain + Hugging Face**")

tab1, tab2 = st.tabs(["💬 Text Chat", "🎨 Image Generation"])

with tab1:
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

with tab2:
    st.subheader("Generate Images from Text")
    
    image_prompt = st.text_area("Describe the image you want to generate:", height=100, placeholder="A serene landscape with mountains and a lake at sunset...")
    
    if st.button("🎨 Generate Image", type="primary"):
        if image_prompt:
            with st.spinner("Creating your image..."):
                image = generate_image(image_prompt)
                if image:
                    st.image(image, caption=image_prompt, use_container_width=True)
                    
                    buf = BytesIO()
                    image.save(buf, format="PNG")
                    st.download_button(
                        label="⬇️ Download Image",
                        data=buf.getvalue(),
                        file_name="generated_image.png",
                        mime="image/png"
                    )
                else:
                    st.error("Failed to generate image. Please try again.")
        else:
            st.warning("Please enter a description first.")

with st.sidebar:
    st.header("Options")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        memory.clear()
        st.rerun()
