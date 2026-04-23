from app.orchestrator import run_pipeline


#text = "I started DrugX last week and now I have severe headaches and nausea. I went to hospital."
text = input().strip()

result = run_pipeline(text)


print("\n--- FINAL OUTPUT ---")
print("DATA:", result["data"])
print("SERIOUSNESS:", result["seriousness"])
print("CAUSALITY:", result["causality"])
print("NARRATIVE:", result["narrative"])
print("SIGNAL:", result["signal"])
