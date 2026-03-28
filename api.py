import requests

def get_stop_data(id: int):
    data = requests.get(f"https://www.zditm.szczecin.pl/api/v1/displays/{id}").json()

    name = data["stop_name"]
    
    departures = []
    for dep in data["departures"]:
        time = dep["time_real"]
        if time == None:
            time = dep["time_scheduled"]
        else: time = f"{time}min"
        obj = {
            "line": dep["line_number"],
            "direction": dep["direction"],
            "time": time,
            }
        departures.append(obj)

    return {"name": name, "departures": departures[:6]}