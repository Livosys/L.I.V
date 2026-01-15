from freshservice.people import search_person
from freshservice.tickets import get_tickets_for_requester, create_ticket
from freshservice.assets import get_assets_for_user

async def handle_person_lookup(query: str):
    persons = await search_person(query)
    if not persons:
        return {"reply": "Hittade ingen person i Freshservice."}

    person = persons[0]
    requester_id = person["id"]

    tickets = await get_tickets_for_requester(requester_id)
    assets = await get_assets_for_user(requester_id)

    return {
        "type": "person_full_info",
        "person": person,
        "tickets": tickets,
        "assets": assets
    }
