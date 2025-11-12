from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from app.memory_manager import memory
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

def get_response(user_input, context=""):
    """Generate response from Hugging Face API"""
    try:
        result = model.invoke(user_input)
        response = result.content
        
        memory.save_context({"input": user_input}, {"output": response})
        
        return response
        
    except Exception as e:
        print(f"API Error: {e}")
        return f"I'm having trouble connecting to the AI model. Please try again."