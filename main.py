from flask import Flask, render_template, jsonify
from bus_api import get_stop_data
from weather_api import get_weather
from datetime import datetime

app = Flask(__name__)

@app.route("/stops/<int:id>")
def stop(id=21313):
    return jsonify(get_stop_data(id))

#this should be written in script.js but i hate javascript
@app.route("/clock/<format>")
def clock(format="H:M"):
    time =datetime.now().time()

    f = "%H:%M"
    match format:
        case "H:M": pass
        case "S": f="%S"

    return time.strftime(f)

@app.route("/weather")
def weather():
    return get_weather()

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)