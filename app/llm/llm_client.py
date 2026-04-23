import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        raise ValueError("GROQ_API_KEY not found in environment or Streamlit secrets")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api_key
)