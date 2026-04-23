from app.Agents.extraction import extract_entities
from app.Agents.medTerminologyMapping import medterminology_mapping
from app.Agents.seriousness import classify_seriousness
from app.Agents.casuality import assess_causality
from app.Agents.narrative import generate_narrative
from app.Agents.signal import detect_signal


def run_pipeline(text: str):

    state = {}
    try:
        data = extract_entities(text)
    except Exception as e:
        print("Extraction failed:", e)
        data = None

    if data is None:
        raise ValueError("Entity extraction failed")

    data = data.model_dump()

    data = medterminology_mapping(data)

    seriousness = classify_seriousness(data)
    data["seriousness"] = seriousness

    causality = assess_causality(data)

    narrative = generate_narrative(data)

    signal = detect_signal(data)

    state["input"] = text
    state["data"] = data
    state["seriousness"] = seriousness
    state["causality"] = causality
    state["narrative"] = narrative
    state["signal"] = signal

    return state
