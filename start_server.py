import json

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


# 1st stage initial calls
@app.route('/api/System/GetPlatformSupportedVersions', methods=['GET'])
def get_platform_supported_versions():
    return "Coming soon"


@app.route('/api/Accounts/CheckSteamAccount', methods=['POST'])
def check_steam_account():
    return "Coming soon"


@app.route('/api/Accounts/RefreshUserDetails', methods=['POST'])
def refresh_user_details():
    return "Coming soon"


@app.route('/api/System/EmergencyMessage', methods=['GET'])
def emergency_message():
    return "Coming soon"


# 2nd stage

@app.route('/api/Accounts/GetUserStats', methods=['POST'])
def get_user_stats():
    return "Coming soon"


@app.route('/api/PlayerStatus/SetPlayerStatus', methods=['POST'])
def set_player_status():
    return jsonify({"payload": {"": ""}})


# 3rd stage
@app.route('/api/Accounts/Login', methods=['POST'])
def login():
    print(request.data)
    response = make_response(jsonify({
        "payload": {"username": "Razbi"}
    }))
    # response.headers["Content-Type"] = "application/json"
    # response.headers["X-Auth-Token"] = "1111111111111111"
    return response


# 4th stage (after login)
@app.route('/api/Friends/Get', methods=['GET'])
def get_friends():
    return jsonify({"payload": {"": ""}})


@app.route('/api/Messaging/GetDirectMessagesFor', methods=['POST'])
def get_direct_messages():
    return jsonify({'payload': {"": ""}})


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
