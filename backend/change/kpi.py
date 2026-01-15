_KPI = []

def record(change_id: str, predicted: dict, actual: dict):
    _KPI.append({
        "change_id": change_id,
        "predicted": predicted,
        "actual": actual
    })

def summary():
    total = len(_KPI)
    correct = sum(
        1 for k in _KPI
        if k["predicted"]["risk_level"] == k["actual"]["risk_level"]
    )
    return {
        "total": total,
        "accuracy": round(correct / total, 2) if total else 0
    }
