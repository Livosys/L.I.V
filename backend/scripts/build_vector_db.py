import json
import os
import numpy as np

# Very simple demo tickets (dummy ITSM data)
TICKETS = [
    {
        "id": 1,
        "text": "User could not send emails because the mailbox was full.",
        "source": "ITSM-001"
    },
    {
        "id": 2,
        "text": "VPN connection failed due to expired user credentials.",
        "source": "ITSM-002"
    },
    {
        "id": 3,
        "text": "Laptop was slow because the disk was almost full.",
        "source": "ITSM-003"
    },
    {
        "id": 4,
        "text": "User could not access SharePoint because permissions were missing.",
        "source": "ITSM-004"
    },
    {
        "id": 5,
        "text": "Email delivery failed because the SMTP service was down.",
        "source": "ITSM-005"
    }
]

OUTPUT_PATH = "data/vector_db.json"


def fake_embedding(text: str, dim: int = 384):
    """
    Placeholder embedding.
    Will be replaced by OpenAI embeddings in step 2.
    """
    np.random.seed(abs(hash(text)) % (2**32))
    return np.random.rand(dim).tolist()


def build_vector_db():
    db = []

    for t in TICKETS:
        db.append({
            "id": t["id"],
            "text": t["text"],
            "source": t["source"],
            "embedding": fake_embedding(t["text"])
        })

    os.makedirs("data", exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(db, f, indent=2)

    print(f"✅ Vector DB created with {len(db)} entries")
    print(f"📁 Saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    build_vector_db()
