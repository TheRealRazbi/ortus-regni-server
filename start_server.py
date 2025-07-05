import json

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


def placeholder():
    return jsonify({'payload': {"": ""}})


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


@app.route('/api/Leaderboard/GetPlacementMatchesRemaining', methods=['POST'])
def get_placement_matches_remaining():
    return placeholder()


def dummy_datetime():
    return "2025-07-05T16:04:00Z"


def dummy_user_id():
    return "some_user_id"


def dummy_steam_id():
    return "some_steam_id"


def dummy_token():
    return "some_dummy_token"


def dummy_user_permissions():
    return {"userpermissions": [dummy_user_permission()]}


def dummy_user_permission():
    return {"privilege": 1, "isenabled": False}


def dummy_registrations():
    return [dummy_registration()]


def dummy_registration():
    return {"userId": dummy_user_id(), "token": dummy_token(), "note": "some_note"}


def dummy_user():
    return {
        "username": "some_dude",
        "password": "qwerty",
        "email": "",
        "userId": dummy_user_id(),
        "authorization": dummy_user_permissions(),
        "registrations": dummy_registrations(),
        "verified": True,
        "status": 1,
        "emailsub": False,
        "steamId": dummy_steam_id(),
    }


def dummy_deck():
    return {}


def dummy_player_match_entry():
    return {
        "color": "green",
        "deck": dummy_deck(),
        "user": dummy_user(),
        "aiType": 0,
        "aiDifficulty": 0,
        "inviteStatus": 2,
        "dead": False,
        "strikes": 0,
        "ready": True,
        "seriesPoints": 3,
        "seriesLocked": False
    }


def dummy_match():
    _me = dummy_player_match_entry
    return {
    }


def dummy_authoritative_match():
    _me = dummy_player_match_entry
    return {
        "offline": False,
        "security": 1,
        "numPlayers": 2,
        "host": _me(),
        "players": [_me(), _me()],
        "match": dummy_match(),
        "currentPlayerId": dummy_user_id(),
        "winningPlayerId": dummy_user_id(),
        "lastActionDate": dummy_datetime(),
        "round": 20,
        "status": 3,
        "sceneName": 1,
        "turntimers": True,
        "tournamentRules": False,
        "gameSeries": False,
    }


def payloadify(data: dict):
    return jsonify({"payload": data})


@app.route('/api/Matches/GetMatches', methods=['POST'])
def get_matches():
    """Each list needs only authoritative matches"""
    print(f"get_matches[request.data]={request.data}")
    return payloadify({
        "invited": [],
        "inlobby": [],
        "inprogress": [],
        "completed": [
            dummy_authoritative_match()
        ],
        "latestmessages": [],
    })


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
