#!/usr/bin/env python3
"""
Test script to validate GPT setup
"""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all required modules can be imported"""
    try:
        from app.config import APP_NAME, HUGGINGFACEHUB_API_TOKEN
        from app.llm_chain import get_response
        from app.memory_manager import memory
        from app.utils import log_message, clean_text
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_config():
    """Test configuration"""
    try:
        from app.config import HUGGINGFACEHUB_API_TOKEN
        if HUGGINGFACEHUB_API_TOKEN:
            print("✅ Hugging Face API token loaded")
            return True
        else:
            print("❌ Hugging Face API token not found")
            return False
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False

def test_basic_response():
    """Test basic LLM response"""
    try:
        from app.llm_chain import get_response
        response = get_response("Hello, how are you?")
        if response:
            print(f"✅ LLM response received: {response[:50]}...")
            return True
        else:
            print("❌ No response from LLM")
            return False
    except Exception as e:
        print(f"❌ LLM error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing GPT Setup...")
    print("-" * 40)
    
    tests = [
        ("Imports", test_imports),
        ("Configuration", test_config),
        ("LLM Response", test_basic_response)
    ]
    
    passed = 0
    for name, test_func in tests:
        print(f"\n🔍 Testing {name}...")
        if test_func():
            passed += 1
    
    print(f"\n📊 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! Your GPT is ready to use.")
        print("🚀 Run: python run_streamlit.py")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")