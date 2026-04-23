from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import run_pipeline

app = FastAPI()


class InputText(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "Pharmacovigilance API is running"}


@app.post("/analyze")
def analyze(input_data: InputText):
    result = run_pipeline(input_data.text)
    return result