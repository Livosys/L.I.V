FEATURES = {
    "rag": True,
    "sla_agent": True,
    "kb_suggestions": True,
    "hitl": True,
    "writeback": False
}

def is_enabled(feature: str) -> bool:
    return FEATURES.get(feature, False)

def require_feature(name: str):
    if not is_enabled(name):
        raise RuntimeError(f"Feature {name} is disabled")
