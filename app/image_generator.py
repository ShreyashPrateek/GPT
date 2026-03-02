from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

def generate_image(prompt, model="black-forest-labs/FLUX.1-schnell"):
    """Generate image from text prompt using Hugging Face"""
    try:
        image = client.text_to_image(prompt, model=model)
        return image
    except Exception as e:
        print(f"Image Generation Error: {e}")
        return None
