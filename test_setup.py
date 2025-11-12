#!/usr/bin/env python3
"""
Test script to verify all dependencies are working correctly
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_imports():
    """Test if all required packages can be imported"""
    try:
        import langchain
        print("✅ LangChain imported successfully")
        
        import langchain_huggingface
        print("✅ LangChain HuggingFace imported successfully")
        
        import transformers
        print("✅ Transformers imported successfully")
        
        import torch
        print("✅ PyTorch imported successfully")
        
        import streamlit
        print("✅ Streamlit imported successfully")
        
        import chromadb
        print("✅ ChromaDB imported successfully")
        
        import faiss
        print("✅ FAISS imported successfully")
        
        import tiktoken
        print("✅ TikToken imported successfully")
        
        import openai
        print("✅ OpenAI imported successfully")
        
        import numpy
        print("✅ NumPy imported successfully")
        
        import pandas
        print("✅ Pandas imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_huggingface_setup():
    """Test HuggingFace setup"""
    try:
        from langchain_huggingface import HuggingFaceEndpoint
        
        # Check if API token is set
        hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if hf_token and hf_token != "hf_your_token_here":
            print("✅ HuggingFace API token is configured")
            
            # Try to create a model instance (this won't make API calls)
            model = HuggingFaceEndpoint(
                repo_id="microsoft/DialoGPT-medium",
                task="text-generation",
                huggingfacehub_api_token=hf_token
            )
            print("✅ HuggingFace model instance created successfully")
            return True
        else:
            print("⚠️  HuggingFace API token not configured. Please update .env file")
            return False
            
    except Exception as e:
        print(f"❌ HuggingFace setup error: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 Testing Python GPT Project Setup")
    print("=" * 50)
    
    # Test Python version
    import sys
    print(f"🐍 Python version: {sys.version}")
    
    # Test imports
    print("\n📦 Testing package imports:")
    imports_ok = test_imports()
    
    # Test HuggingFace setup
    print("\n🤗 Testing HuggingFace setup:")
    hf_ok = test_huggingface_setup()
    
    # Summary
    print("\n" + "=" * 50)
    if imports_ok:
        print("✅ All packages imported successfully!")
        if hf_ok:
            print("✅ Setup is complete and ready to use!")
        else:
            print("⚠️  Setup is mostly complete. Please configure your HuggingFace API token in .env file")
    else:
        print("❌ Some packages failed to import. Please check the installation.")

if __name__ == "__main__":
    main()