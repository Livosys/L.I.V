from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -----------------------------
# GET TICKET (dummy placeholder)
# -----------------------------
def get_ticket(ticket_id: int):
    # Här ska du koppla Freshservice senare.
    # Just nu returnerar vi dummy-data så API:n funkar.
    return {
        "id": ticket_id,
        "subject": "Test ticket subject",
        "description": "This is a dummy ticket description for testing.",
        "priority": "Medium"
    }


# -----------------------------
# ANALYZE TICKET (NEW OPENAI API)
# -----------------------------
def analyze_ticket(ticket):
    prompt = f"""
    You are an ITSM expert. Analyze the following ticket:

    Subject: {ticket['subject']}
    Description: {ticket['description']}
    Priority: {ticket['priority']}

    Provide a structured analysis.
    """

    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You analyze Freshservice tickets."},
            {"role": "user", "content": prompt}
        ]
    )

    # NEW WAY (correct for 2024+ OpenAI SDK)
    return completion.choices[0].message.content


# -----------------------------
# UPDATE TICKET (dummy placeholder)
# -----------------------------
def update_ticket(ticket_id: int, analysis: str):
    # Här bygger vi senare Freshservice-uppdateringen.
    return {
        "status": "OK",
        "ticket_id": ticket_id,
        "analysis_saved": True,
        "analysis": analysis
    }
