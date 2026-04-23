EXTRACTION_PROMPT = """
You are an information extraction system.

Return ONLY valid JSON. No code. No explanation.

Output format:
{{
  "drug": "string",
  "events": ["string"],
  "severity": "low | medium | high",
  "hospitalization": true or false,
  "timeline": "string"
}}

Example:
Text: I took DrugY and had mild headache.
Output:
{{
  "drug": "DrugY",
  "events": ["headache"],
  "severity": "low",
  "hospitalization": false,
  "timeline": "unknown"
}}

Now extract:

Text:
{text}
"""


MAPPING_PROMPT = """
You are a medical terminology expert.

Map symptoms to MedDRA Preferred Terms (PT).

Return ONLY a JSON array.

Format:
[
  {{
    "original": "string",
    "meddra_pt": "STRING"
  }}
]

Rules:
- Use uppercase MedDRA terms
- Keep terms simple (1-2 words)
- Do NOT return code
- Do NOT explain anything

Example:
Input: ["headache", "nausea"]

Output:
[
  {{
    "original": "headache",
    "meddra_pt": "HEADACHE"
  }},
  {{
    "original": "nausea",
    "meddra_pt": "NAUSEA"
  }}
]

Now map:

Input:
{events}
"""


SERIOUSNESS_PROMPT = """
Classify the following case as SERIOUS or NON-SERIOUS.

Return ONLY JSON:

{{
  "label": "SERIOUS or NON-SERIOUS",
  "confidence": 0.xx,
  "reason": "short reason"
}}

Rules:
- Hospitalization means SERIOUS
- Otherwise decide based on severity and symptoms
- Do NOT return code
- Do NOT explain outside JSON

Data:
{data}
"""


CAUSALITY_PROMPT = """
Assess causality between the drug and events.

Return ONLY JSON:

{{
  "causality": "probable | possible | unlikely",
  "confidence": 0.xx,
  "reasons": ["short reasons"]
}}

Data:
{data}
"""
