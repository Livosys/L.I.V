from .client import fresh

async def get_assets_for_user(user_id: int):
    params = {"user_id": user_id}
    data = await fresh.get("/api/v2/assets", params=params)
    return data.get("assets", [])
