from dataclasses import dataclass
from datetime import date
from enum import Enum


@dataclass(frozen=True)
class Team(object):
    name: str


@dataclass(frozen=True)
class Fixture(object):
    home_team: Team
    away_team: Team
    league: str


@dataclass(frozen=True)
class Scenario(object):
    minutes_elapsed: int
    home_goals: int
    away_goals: int


class Outcome(str, Enum):
    HOME = "home"
    AWAY = "away"
    DRAW = "draw"


@dataclass
class Result(object):
    fixture: Fixture
    outcome: Outcome
    home_goals: int
    away_goals: int
    season: int
    home_spi: float
    away_spi: float
    match_date: date
