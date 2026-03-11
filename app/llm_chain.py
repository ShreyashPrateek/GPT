from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from app.memory_manager import memory
from app.web_search import search_web, needs_web_search
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

def get_response(user_input, context=""):
    """Generate response from Hugging Face API with web search capability"""
    try:
        # Check if web search is needed
        if needs_web_search(user_input):
            search_results = search_web(user_input)
            
            # Create a more explicit prompt
            enhanced_input = f"""You are a helpful AI assistant with access to current information.

User's question: {user_input}

Current web search results:
{search_results}

IMPORTANT: Use ONLY the information from the web search results above to answer the question. If the search results say the event hasn't happened yet or no information is available, clearly state that. Do not use your training data for this answer.

Answer:"""
            result = model.invoke(enhanced_input)
        else:
            result = model.invoke(user_input)
        
        response = result.content
        
        memory.save_context({"input": user_input}, {"output": response})
        
        return response
        
    except Exception as e:
        print(f"API Error: {e}")
        return f"I'm having trouble connecting to the AI model. Please try again."