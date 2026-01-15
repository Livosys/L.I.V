import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

BASE = Path(__file__).parent
DATA = json.loads((BASE / "synthetic.json").read_text())

X = [row["text"] for row in DATA]
y = [row["intent"] for row in DATA]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

with open(BASE / "intent_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)
