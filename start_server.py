import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/", methods=["GET"])
def root():
    return jsonify({"message": "Ortus Regni Server Active"})


def main():
    with open("config.json", "r") as f:
        config = json.load(f)
        if "server" not in config:
            raise FileNotFoundError("No server found in config.json")
        port = config["server"].get("port", 45632)
    app.run(port=port, debug=True)


if __name__ == "__main__":
    main()
