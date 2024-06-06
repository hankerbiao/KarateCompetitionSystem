from enum import Enum


class SexEnum(str, Enum):
    MALE = 0
    FEMALE = 1


class ColorEnum(str, Enum):
    RED = 0
    CYAN = 1


class MatchUpdateType(str, Enum):
    score = "score"
    foul = "foul"
