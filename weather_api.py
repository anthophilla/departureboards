import requests

def match_weather_code(code: int) -> chr:
    WEATHER_MAP = {
        # clear / clouds
        0: "☀",   # clear
        1: "🌤",   # mainly clear
        2: "⛅",   # partly cloudy
        3: "☁",   # overcast

        # fog
        45: "🌫",
        48: "🌫",

        # drizzle
        51: "🌦",
        53: "🌦",
        55: "🌧",

        # rain
        61: "🌧",
        63: "🌧",
        65: "🌧",

        # freezing rain
        66: "🌧",
        67: "🌧",

        # snow
        71: "❄",
        73: "❄",
        75: "❄",
        77: "❄",

        # showers
        80: "🌧",
        81: "🌧",
        82: "🌧",

        # snow showers
        85: "❄",
        86: "❄",

        # thunder
        95: "⛈",
        96: "⛈",
        99: "⛈",
    }
    return WEATHER_MAP.get(code, '?')

def get_weather():
    data = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 53.4289,
            "longitude": 14.553,
            "current_weather": True
        }
    ).json()
    temperature = data["current_weather"]["temperature"]
    emoji = match_weather_code(int(data["current_weather"]["weathercode"]))
    return f"{temperature}°C {emoji} "

#print(get_weather())