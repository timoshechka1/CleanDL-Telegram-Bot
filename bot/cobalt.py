import requests

COBALT_API_URL = "https://api.cobalt.tools/"
COBALT_HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJrTzZodEpnaiIsInN1YiI6IkF2SGZYMmYxIiwiZXhwIjoxNzQ1NDg5NDI5fQ.9FmAL09xPtcyfwpzd0SG1n4qONrTAWwPk07NffzHAjU",
    "Content-Type": "application/json",
}

def get_direct_video_url(video_url: str) -> str | None:
    payload = {"url": video_url}
    try:
        print("[DEBUG] Отправляем запрос с payload:", payload)
        response = requests.post(COBALT_API_URL, headers=COBALT_HEADERS, json=payload)
        print("[DEBUG] Статус код ответа:", response.status_code)
        print("[DEBUG] Тело ответа:", response.text)
        response.raise_for_status()
        data = response.json()
        return data.get("url")
    except Exception as e:
        print(f"[ERROR] Не удалось получить ссылку на видео: {e}")
        return None