import os
import httpx

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

def get_weather(city: str) -> dict:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "en"
    }

    response = httpx.get(url, params=params, timeout=10.0)

    if response.status_code == 404:
        raise ValueError(f"City '{city}' not found.")
    if response.status_code == 401:
        raise ValueError("Invalid API key.")
    if response.status_code != 200:
        raise ValueError(f"Weather API error (HTTP {response.status_code}).")

    data = response.json()
    return {
        "temperature_celsius": round(data["main"]["temp"], 1),
        "conditions": data["weather"][0]["description"].capitalize(),
    }