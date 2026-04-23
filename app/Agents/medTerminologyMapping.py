from langchain_core.prompts import PromptTemplate
from app.llm.ollama_cli import llm
from app.llm.prompts import MAPPING_PROMPT
import json
import re


def clean_json(text):
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if match:
        return match.group(0)
    return text


prompt = PromptTemplate(
    template=MAPPING_PROMPT,
    input_variables=["events"]
)

def medterminology_mapping(data):
    events = data.get("events", [])

    raw_output = (prompt | llm).invoke({
        "events": events
    })

    try:
        cleaned = clean_json(raw_output)
        mapped = json.loads(cleaned)

        if isinstance(mapped, list):
            data["events"] = [
                {
                    "original": item.get("original", ""),
                    "meddra_pt": item.get("meddra_pt") or item.get("Mapped") or item.get("mapped") or "",
                }
                for item in mapped
                if isinstance(item, dict)
            ]
            return data

    except Exception as e:
        print("Mapping error:", e)
        print("Raw output:", raw_output)

    data["events"] = [
        {"original": e, "meddra_pt": e.upper()}
        for e in events
    ]

    return data
