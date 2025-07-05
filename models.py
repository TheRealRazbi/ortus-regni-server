import json
from enum import IntEnum, auto
from typing import Optional

from pydantic import BaseModel, Field


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
    password: Optional[str] = "qwerty"
    email: str = ""
    userId: str = Field(default_factory=dummy_user_id)
    authorization: Optional[Authorization] = Field(default_factory=Authorization)
    registrations: Optional[list[Registration]] = Field(default_factory=lambda: [Registration()])
    verified: bool = True
    status: int = 1
    emailsub: bool = False
    steamId: Optional[str] = Field(default_factory=dummy_steam_id)


# noinspection PyDataclass
class Deck(BaseModel):
    v: int = 1  # unknown
    f: int = 3  # unknown
    d: str = ""  # the deck itself serialized in some way


# noinspection PyDataclass
class PlayerMatchEntry(BaseModel):
    color: int = 4
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


class MatchStatus(IntEnum):
    Created = auto()
    Waiting = auto()
    InProgress = auto()
    Complete = auto()
    Cancelled = auto()


# noinspection PyDataclass
# noinspection PyDataclass
class AuthoritativeMatch(BaseModel):
    offline: bool = False
    security: int = 1
    numPlayers: int = 2
    host: PlayerMatchEntry
    players: list[PlayerMatchEntry] = Field(default_factory=list)
    match: dict = Field(default_factory=dict)
    currentPlayerId: str = Field(default_factory=dummy_user_id)
    winningPlayerId: str = Field(default_factory=dummy_user_id)
    lastActionDate: str = Field(default_factory=dummy_datetime)
    round: int = 20
    status: int = MatchStatus.Created.value
    sceneName: int = 1
    turntimers: bool = True
    tournamentRules: bool = False
    gameSeries: bool = False

    @classmethod
    def from_match_settings(cls, settings: 'MatchSettings'):
        match_obj = Match()
        match_id, archived = archive_object(match_obj, "Match", "match_1")
        archived_payload = json.dumps({
            "data": {match_id: archived},
            "$root": {"$ref": match_id}
        })
        return cls(
            security=settings.security,
            numPlayers=settings.players,
            host=settings.host,
            players=[],
            match={"v": 1, "f": 3, "d": archived_payload},
            currentPlayerId=dummy_user_id(),
            winningPlayerId=dummy_user_id(),
            lastActionDate=dummy_datetime(),
            round=20,
            status=MatchStatus.Created.value,
            sceneName=settings.sceneName,
            turntimers=settings.turntimers,
            tournamentRules=settings.tournamentRules,
            gameSeries=settings.gameSeries
        )


# noinspection PyDataclass
class MatchSettings(BaseModel):
    security: int
    players: int
    host: PlayerMatchEntry
    sceneName: int
    turntimers: bool
    tournamentRules: bool
    gameSeries: bool


def archive_object(obj, obj_type: str, id_: str):
    return id_, {
        "$type": obj_type,
        **obj.model_dump()
    }
