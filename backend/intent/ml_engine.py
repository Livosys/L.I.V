import pickle
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "intent_model.pkl"

_model = None

def predict_intent(text: str):
    global _model
    if not MODEL_PATH.exists():
        return None

    if _model is None:
        with open(MODEL_PATH, "rb") as f:
            vectorizer, model = pickle.load(f)
            _model = (vectorizer, model)

    vectorizer, model = _model
    X = vectorizer.transform([text])
    intent = model.predict(X)[0]
    return intent
