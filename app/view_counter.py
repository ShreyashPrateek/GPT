import json
import os
from threading import Lock

COUNTER_FILE = "data/view_counter.json"
lock = Lock()

def ensure_counter_file():
    os.makedirs(os.path.dirname(COUNTER_FILE), exist_ok=True)
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'w') as f:
            json.dump({"views": 0}, f)

def get_view_count():
    ensure_counter_file()
    try:
        with lock:
            with open(COUNTER_FILE, 'r') as f:
                data = json.load(f)
                return data.get("views", 0)
    except:
        return 0

def increment_view_count():
    ensure_counter_file()
    try:
        with lock:
            with open(COUNTER_FILE, 'r') as f:
                data = json.load(f)
            
            data["views"] = data.get("views", 0) + 1
            
            with open(COUNTER_FILE, 'w') as f:
                json.dump(data, f)
            
            return data["views"]
    except:
        return 0
