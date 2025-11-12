#!/usr/bin/env python3
"""
Startup script for the GPT application
"""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    print("🚀 Starting Custom GPT Application...")
    print("=" * 50)
    
    try:
        # Import and run the Flask interface
        from ui.interface import app
        print("✅ Flask interface loaded successfully")
        print("🌐 Starting web server at http://localhost:5000")
        print("💡 Open your browser and go to: http://localhost:5000")
        print("=" * 50)
        
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down GPT application...")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print("💡 Make sure you have activated your virtual environment:")
        print("   source .venv/bin/activate")

if __name__ == "__main__":
    main()