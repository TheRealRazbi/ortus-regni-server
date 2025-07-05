import json

from flask import Flask, request, jsonify, make_response

from models import MatchSettings

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


def payloadify(data: dict):
    return jsonify({"payload": data})


@app.route('/api/Matches/GetMatches', methods=['POST'])
def get_matches():
    """Each list needs only authoritative matches"""
    # print(f"get_matches[request.data]={request.data}")
    return payloadify({
        "invited": [],
        "inlobby": [],
        "inprogress": [],
        "completed": [],
        "latestmessages": [],
    })


@app.route('/api/Matches/Create', methods=['POST'])
def create_match():
    settings = MatchSettings(**request.json)
    print(settings)

    # print(f"create_match[request.data]={request.data}")
    return payloadify({}), 400


@app.route('/api/Matches/GetState', methods=['POST'])
def get_match_state():
    # if request.data:
    #     print(f"get_state[request.data]={request.data}")
    return payloadify({})
# {'gameSeries': False, 'host': {'aiDifficulty': 0, 'aiType': 0, 'color': 5, 'dead': False, 'deck': {'d': '{"data":{"$root":{"$ref":"658340544"},"658340544":{"$type":"Deck","g":null,"d":"Unselected","n":"All Rounder Politics Heavy","t":"NotPrebuilt","c":[{"$ref":"309218413"},{"$ref":"1754424091"},{"$ref":"477948119"},{"$ref":"410808345"},{"$ref":"-2003313471"},{"$ref":"1360131012"},{"$ref":"1202840620"},{"$ref":"2126534164"},{"$ref":"905278835"},{"$ref":"100327309"},{"$ref":"839155546"},{"$ref":"1104472179"},{"$ref":"321214170"},{"$ref":"-1641809738"},{"$ref":"1333233006"},{"$ref":"1283465387"},{"$ref":"1367922650"},{"$ref":"-886041981"},{"$ref":"-1775494301"},{"$ref":"-2140653862"},{"$ref":"865791316"},{"$ref":"1017725706"},{"$ref":"-480078102"},{"$ref":"1356719986"}],"r":{"$ref":"-342259072"}},"309218413":{"$type":"Card","g":"cbebc80f-b29a-47d2-a508-32e6aaca6683","c":"Land","d":{"$ref":"658340544"}},"1754424091":{"$type":"Card","g":"6ccdd65b-0052-4a3c-bf6a-563f741fd902","c":"Land","d":{"$ref":"658340544"}},"477948119":{"$type":"Card","g":"9aac908a-99eb-4828-9970-47b016d6f9fd","c":"Land","d":{"$ref":"658340544"}},"410808345":{"$type":"Card","g":"ba26a80e-447f-4000-8d13-236d336fc9c9","c":"Vassal","d":{"$ref":"658340544"}},"-2003313471":{"$type":"Card","g":"6d93b5fb-8bff-4606-8c4f-54ae337f0e13","c":"Vassal","d":{"$ref":"658340544"}},"1360131012":{"$type":"Card","g":"fb508a52-d143-4c05-a289-ede1b543ace7","c":"Vassal","d":{"$ref":"658340544"}},"1202840620":{"$type":"Card","g":"ba4f297e-ea5e-4153-ae29-8dba306c6bef","c":"Treachery","d":{"$ref":"658340544"}},"2126534164":{"$type":"Card","g":"845ea781-d514-475b-bf45-2e3997fe2938","c":"Treachery","d":{"$ref":"658340544"}},"905278835":{"$type":"Card","g":"c115bfba-d488-4097-9102-c549cb71e4f5","c":"Treachery","d":{"$ref":"658340544"}},"100327309":{"$type":"Card","g":"5d310456-0eb9-424f-9534-3e1ad6aacc22","c":"Banner","d":{"$ref":"658340544"}},"839155546":{"$type":"Card","g":"7754be3c-0f93-48fd-8e69-a0d9123cb102","c":"Banner","d":{"$ref":"658340544"}},"1104472179":{"$type":"Card","g":"8eec7d21-0906-4888-a0d8-52083dbe4e88","c":"Banner","d":{"$ref":"658340544"}},"321214170":{"$type":"Card","g":"f0ea2300-41c4-43e8-a2d1-a6285777105f","c":"Castle","d":{"$ref":"658340544"}},"-1641809738":{"$type":"Card","g":"fd7c6aa7-bee8-4a9c-a5d7-db641ca1476f","c":"Castle","d":{"$ref":"658340544"}},"1333233006":{"$type":"Card","g":"d01d527f-39e7-4d2f-867f-9ce10f122d27","c":"Marketplace","d":{"$ref":"658340544"}},"1283465387":{"$type":"Card","g":"fb04f156-520e-4a90-81a4-c014167f8580","c":"Marketplace","d":{"$ref":"658340544"}},"1367922650":{"$type":"Card","g":"f42a8747-90ae-4e02-bb62-65d2c656e98b","c":"Prince","d":{"$ref":"658340544"}},"-886041981":{"$type":"Card","g":"d4233ca1-d35d-4a07-9fc2-bcc1c73aef28","c":"Prince","d":{"$ref":"658340544"}},"-1775494301":{"$type":"Card","g":"b6103375-ffa2-419a-a80c-a415fd3bcd58","c":"Counter","d":{"$ref":"658340544"}},"-2140653862":{"$type":"Card","g":"499c83d4-f43b-40c1-af6b-f78a00d089fc","c":"Counter","d":{"$ref":"658340544"}},"865791316":{"$type":"Card","g":"d848cbdb-3afe-4ed5-b629-679a889ef259","c":"Intrigue","d":{"$ref":"658340544"}},"1017725706":{"$type":"Card","g":"d3ff2ca1-c67a-45f9-a969-2b3f0bcacbd0","c":"Intrigue","d":{"$ref":"658340544"}},"-480078102":{"$type":"Card","g":"1d85d994-1c38-42d6-bd2b-0b0d92575aa7","c":"Church","d":{"$ref":"658340544"}},"1356719986":{"$type":"Card","g":"8581d0e3-8aa9-4bae-9ca9-eaeac9e815e3","c":"Cathedral","d":{"$ref":"658340544"}},"-342259072":{"$type":"OrtusRandom","i":0,"seed":"2612604689641009696","x":"2612604689641009696","y":"1260646213","z":"607240589","w":"1050288779","v":"0"}}}', 'f': 3, 'v': 1}, 'inviteStatus': 0, 'ready': False, 'seriesLocked': False, 'seriesPoints': 0, 'strikes': 0, 'user': {'authorization': None, 'email': '', 'emailsub': False, 'password': None, 'registrations': None, 'status': 0, 'steamId': None, 'userId': '', 'username': '', 'verified': False}}, 'players': 2, 'sceneName': 2, 'security': 1, 'tournamentRules': False, 'turntimers': False}

@app.route('/api/Messaging/GetMatchMessages', methods=['POST'])
def get_match_messages():
    # if request.data:
    #     print(f"get_match_messages[request.data]={request.data}")
    return payloadify({})


@app.route("/api/", methods=["GET"])
def root():
    return jsonify({"message": "Ortus Regni Server Active"})


def main():
    with open("config.json", "r") as f:
        config = json.load(f)
        if "server" not in config:
            raise FileNotFoundError("No server found in config.json")
        port = config["server"].get("port", 45632)
    app.run(port=port, debug=True, use_reloader=False)


if __name__ == "__main__":
    main()
