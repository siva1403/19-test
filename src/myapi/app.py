from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Python API is running",
        "message": "Edited by Vijay",
        "timestamp": datetime.now().strftime("%H:%M:%S %d %b %Y")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
