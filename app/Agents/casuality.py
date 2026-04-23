from langchain_core.prompts import PromptTemplate
from app.llm.llm_client import llm
from app.llm.prompts import CAUSALITY_PROMPT
import json
import re


def clean_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text


prompt = PromptTemplate(
    template=CAUSALITY_PROMPT,
    input_variables=["data"]
)


def assess_causality(data):

    timeline = data.get("timeline")
    seriousness = data.get("seriousness", {}).get("label")

    if timeline and seriousness == "SERIOUS":
        return {
            "causality": "probable",
            "confidence": 0.85,
            "reasons": ["Temporal relationship present", "Serious event"]
        }

    if timeline:
        return {
            "causality": "possible",
            "confidence": 0.7,
            "reasons": ["Temporal relationship present"]
        }

    raw_output = (prompt | llm).invoke({
        "data": str(data)
    })

    try:
        # Extract content from AIMessage object
        raw_text = raw_output.content if hasattr(raw_output, 'content') else str(raw_output)
        cleaned = clean_json(raw_text)
        return json.loads(cleaned)
    except:
        return {
            "causality": "unlikely",
            "confidence": 0.5,
            "reasons": ["Insufficient data"]
        }