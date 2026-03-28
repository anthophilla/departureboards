import requests
from datetime import datetime, timedelta

def format_seconds(seconds: int):
    if seconds>3600:
        return f"{seconds//3600}h {(seconds%3600)//60}min"
    else:
        return f"{seconds//60}min"

def get_stop_data(id: int):
    data = requests.get(f"https://www.zditm.szczecin.pl/api/v1/displays/{id}").json()

    name = data["stop_name"]
    
    departures = []
    for dep in data["departures"]:
        time = dep["time_real"]
        # format time bc it can return 5min or an exact hour of arrival like 16:32
        if time == None:
            #print(dep["time_scheduled"])
            now = datetime.now()
            t = datetime.strptime(dep["time_scheduled"], '%H:%M').time()
            target = datetime.combine(now.date(), t)
            if target < now:
                target += timedelta(days=1)
            
            time = format_seconds((target - now).seconds)
        else: time = f"{time}min"

        obj = {
            "line": dep["line_number"],
            "direction": dep["direction"],
            "time": time,
            }
        departures.append(obj)

    return {"name": name, "departures": departures[:6]}