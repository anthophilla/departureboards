from flask import Flask, render_template, jsonify
from api import get_stop_data

app = Flask(__name__)

@app.route("/stops/<int:id>")
def stop(id=21313):
    return jsonify(get_stop_data(id))

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)