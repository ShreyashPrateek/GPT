from typing import Dict, List, Any

class SimpleMemory:
    """Simple memory implementation for conversation history"""
    
    def __init__(self):
        self.chat_memory = []
    
    @property
    def memory_variables(self) -> List[str]:
        return ["history"]
    
    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return {"history": self.buffer_as_str}
    
    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        self.chat_memory.append(f"Human: {inputs['input']}")
        self.chat_memory.append(f"AI: {outputs['output']}")
    
    def clear(self) -> None:
        self.chat_memory = []
    
    @property
    def buffer_as_str(self) -> str:
        return "\n".join(self.chat_memory[-6:])  # Keep last 3 exchanges

memory = SimpleMemory()