import os
from dotenv import load_dotenv

load_dotenv()

# Test API connection
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print(f"API Token exists: {bool(api_token)}")
print(f"API Token length: {len(api_token) if api_token else 0}")

try:
    from langchain_huggingface import HuggingFaceEndpoint
    print("✅ HuggingFaceEndpoint imported successfully")
    
    # Test simple model
    llm = HuggingFaceEndpoint(
        repo_id="google/flan-t5-small",
        huggingfacehub_api_token=api_token,
        max_new_tokens=50
    )
    print("✅ LLM initialized successfully")
    
    # Test direct invoke
    response = llm.invoke("What is 2+2?")
    print(f"✅ Direct response: {response}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()