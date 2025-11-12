#!/usr/bin/env python3
"""
Main Streamlit app entry point for deployment
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the interface content
exec(open('ui/interface.py').read())