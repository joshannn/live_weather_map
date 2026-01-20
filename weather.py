import requests, threading, time
from utils import get_temp_color

weather_codes = {
    0: "Clear", 1: "Clear", 2: "Partly Cloudy", 3: "Cloudy",
    45: "Foggy", 48: "Foggy", 51: "Drizzle", 53: "Drizzle",
    55: "Drizzle", 61: "Rainy", 63: "Rainy", 65: "Heavy Rain",
    71: "Snowy", 73: "Snowy", 75: "Heavy Snow", 77: "Snow",
    80: "Showers", 81: "Showers", 82: "Heavy Showers",
    95: "Thunderstorm", 96: "Thunderstorm", 99: "Thunderstorm"
}

def fetch_weather(lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        data = requests.get(url, timeout=5).json()['current_weather']
        return {
            "temp": data['temperature'],
            "temp_str": f"{data['temperature']}°C",
            "condition": weather_codes.get(data['weathercode'], "Overcast"),
            "wind": data.get('windspeed', 0),
            "status": "ready"
        }
    except Exception:
        return {"temp": None, "temp_str": "N/A", "condition": "Offline", "wind": 0, "status": "error"}

def fetch_all_weather(districts, refresh_interval=1800):
    """Fetch all districts periodically"""
    def worker(d):
        w = fetch_weather(d['lat'], d['lon'])
        d['weather_base'] = w
        d['color'] = get_temp_color(w['temp'])
        time.sleep(0.1)

    while True:
        threads = []
        for d in districts:
            t = threading.Thread(target=worker, args=(d,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        time.sleep(refresh_interval)
