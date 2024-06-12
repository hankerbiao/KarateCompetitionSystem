from enum import Enum, IntEnum


class SexEnum(str, Enum):
    MALE = 0
    FEMALE = 1


class ColorEnum(str, Enum):
    RED = 0
    CYAN = 1


class MatchUpdateType(str, Enum):
    score = "score"
    foul = "foul"


class MatchStatus(IntEnum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2


class AthleteStatus(IntEnum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    ELIMINATED = -1
