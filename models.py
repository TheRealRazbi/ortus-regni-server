from pydantic import BaseModel, Field, model_validator


def dummy_datetime():
    return "2025-07-05T16:04:00Z"


def dummy_user_id():
    return "some_user_id"


def dummy_steam_id():
    return "some_steam_id"


def dummy_token():
    return "some_dummy_token"


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
