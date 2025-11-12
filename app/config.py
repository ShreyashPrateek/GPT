import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "SP | GPT"
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
