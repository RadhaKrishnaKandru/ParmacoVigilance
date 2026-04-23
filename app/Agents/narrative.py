def generate_narrative(data):

    drug = data.get("drug")
    events = [e["original"] for e in data.get("events", [])]
    timeline = data.get("timeline", "")
    seriousness = data.get("seriousness", {})

    if len(events) == 1:
        events_text = events[0]
    else:
        events_text = ", ".join(events[:-1]) + " and " + events[-1]

    severity = data.get("severity", "")
    severity_text = "severe" if severity == "high" else severity

    if seriousness.get("label") == "SERIOUS":
        outcome = "requiring hospitalization"
    else:
        outcome = ""

    narrative = f"A patient reported {severity_text} {events_text} following initiation of {drug} {timeline}"

    if outcome:
        narrative += f", {outcome}"

    narrative += "."

    return narrative