from langchain_core.prompts import PromptTemplate
from app.llm.ollama_cli import llm
from app.llm.prompts import SERIOUSNESS_PROMPT
import json
import re


def clean_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text

prompt = PromptTemplate(
    template=SERIOUSNESS_PROMPT,
    input_variables=["data"]
)


def classify_seriousness(data):

    
    if data.get("hospitalization", False):
        return {
            "label": "SERIOUS",
            "confidence": 0.95,
            "reason": "Hospitalization reported"
        }

    
    raw_output = (prompt | llm).invoke({
        "data": str(data)
    })

    try:
        cleaned = clean_json(raw_output)
        result = json.loads(cleaned)

        if "label" in result:
            return result

    except Exception as e:
        print("Seriousness parsing error:", e)
        print("Raw output:", raw_output)

  
    return {
        "label": "NON-SERIOUS",
        "confidence": 0.5,
        "reason": "Fallback default"
    }
