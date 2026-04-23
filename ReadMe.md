# Pharmacovigilance Safety Signal System

An AI-powered system to detect, classify, and prioritize drug safety signals from patient-reported data using an agent-based architecture.

## Overview

This project simulates a real-world pharmacovigilance pipeline used in healthcare and regulatory systems.

It processes patient narratives and performs:

- Entity extraction: drug, symptoms, severity, hospitalization, and timeline
- Medical terminology mapping in a MedDRA-style format
- Seriousness classification
- Signal detection across reports
- Regulatory-style narrative generation
- Causality assessment

## Architecture

```text
User Input
  |
  v
FastAPI Backend
  |
  v
Orchestrator
  |
  v
Agents Pipeline:
  - Entity Extraction
  - Terminology Mapping
  - Seriousness Classification
  - Signal Detection
  - Narrative Generation
  - Causality Assessment
  |
  v
Structured Output
```

## Features

- Extract drug, adverse events, severity, and timeline
- Map symptoms to standardized medical terms
- Classify seriousness as serious or non-serious
- Detect repeated drug-event safety signals
- Generate a clinical narrative
- Assess causality as possible, probable, or unlikely
- FastAPI backend
- Streamlit frontend

## Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- Ollama
- Pydantic

## Installation

```bash
git clone <repo-url>
cd ParmacoVigilance
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
ollama pull llama3.2:3b
```

## Run

Start the API:

```bash
uvicorn app.api:app --reload
```

Start the Streamlit UI in another terminal:

```bash
streamlit run app/app.py
```

The Streamlit app sends analysis requests to `http://127.0.0.1:8000/analyze`.
