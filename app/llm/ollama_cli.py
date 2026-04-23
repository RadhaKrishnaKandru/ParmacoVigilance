from langchain_ollama.llms import OllamaLLM

llm = OllamaLLM(
    model="llama3.2:3b",
    temperature=0
)