import aiohttp

APT_URL = "https://api.cobalt.tools/"

async def fetch_cobalt_data(file_url: str) -> dict:
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "url": file_url,
        "vt": False
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(APT_URL, json=payload, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                return {"error": f"Ошибка: {response.status}"}