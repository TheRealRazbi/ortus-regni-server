from pydantic import BaseModel, Field, model_validator


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


class UserPermission(BaseModel):
    privilege: int = 1
    isenabled: bool = False


class Registration(BaseModel):
    userId: str = Field(default_factory=dummy_user_id)
    token: str = Field(default_factory=dummy_token)
    note: str = "some_note"


# noinspection PyDataclass
class Authorization(BaseModel):
    userpermissions: list[UserPermission] = Field(default_factory=lambda: [UserPermission()])


# noinspection PyDataclass
class User(BaseModel):
    username: str = "some_dude"
    password: str = "qwerty"
    email: str = ""
    userId: str = Field(default_factory=dummy_user_id)
    authorization: Authorization = Field(default_factory=Authorization)
    registrations: list[Registration] = Field(default_factory=lambda: [Registration()])
    verified: bool = True
    status: int = 1
    emailsub: bool = False
    steamId: str = Field(default_factory=dummy_steam_id)


# noinspection PyDataclass
class Deck(BaseModel):
    ...


# noinspection PyDataclass
class PlayerMatchEntry(BaseModel):
    color: str = "green"
    deck: Deck = Field(default_factory=Deck)
    user: User = Field(default_factory=User)
    aiType: int = 0
    aiDifficulty: int = 0
    inviteStatus: int = 2
    dead: bool = False
    strikes: int = 0
    ready: bool = True
    seriesPoints: int = 3
    seriesLocked: bool = False


# noinspection PyDataclass
class Match(BaseModel):
    ...


# noinspection PyDataclass
class AuthoritativeMatch(BaseModel):
    offline: bool = False
    security: int = 1
    numPlayers: int = 2
    host: PlayerMatchEntry = Field(default_factory=PlayerMatchEntry)
    players: list[PlayerMatchEntry] = Field(default_factory=lambda: [PlayerMatchEntry(), PlayerMatchEntry()])
    match: Match = Field(default_factory=Match)
    currentPlayerId: str = Field(default_factory=dummy_user_id)
    winningPlayerId: str = Field(default_factory=dummy_user_id)
    lastActionDate: str = Field(default_factory=dummy_datetime)
    round: int = 20
    status: int = 3
    sceneName: int = 1
    turntimers: bool = True
    tournamentRules: bool = False
    gameSeries: bool = False
