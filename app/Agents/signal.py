from collections import defaultdict

REPORTS = []

def extract_pairs(data):
    pairs = []
    drug = data["drug"]

    for event in data["events"]:
        pt = event.get("meddra_pt", "").upper()
        pairs.append((drug, pt))

    return pairs


def detect_signal(data, threshold=5):

    REPORTS.append(data)

    pair_counts = defaultdict(int)
    serious_counts = defaultdict(int)

    for report in REPORTS:
        pairs = extract_pairs(report)

        for pair in pairs:
            pair_counts[pair] += 1

            # ✅ FIXED
            if "seriousness" in report:
                if report["seriousness"].get("label") == "SERIOUS":
                    serious_counts[pair] += 1

    current_pairs = extract_pairs(data)

    signals = []

    for pair in current_pairs:
        total = pair_counts[pair]
        serious = serious_counts[pair]

        if total >= threshold:
            signals.append({
                "drug": pair[0],
                "event": pair[1],
                "report_count": total,
                "serious_count": serious,
                "signal": True,
                "strength": "moderate" if total < 10 else "strong"
            })

    if not signals:
        return [{"signal": False}]

    return signals