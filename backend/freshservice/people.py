from .client import fresh

async def search_person(query: str):
    params = {"search": query}
    data = await fresh.get("/api/v2/requesters", params=params)
    return data.get("requesters", [])
