from dotenv import load_dotenv
import os

load_dotenv()  # carga el .env automáticamente

GROQ_API_KEY = os.getenv("GROQ_API_KEY")