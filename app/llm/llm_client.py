from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)