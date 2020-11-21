import time

from chess.models.entities.round import Round
from chess.models.entities.player import Player
from chess.models.entities.time_method import TimeMethod


class Tournament:
    def __init__(self, id: int, name: str, location: str, start_date_timestamp: time, end_date_timestamp: time, round_count: int, rounds: list[Round], players: str[Player], time_method: TimeMethod, description: str):
        self.id: int = id
        self.name: str = name
        self.location: str = location
        self.start_date_timestamp: time = start_date_timestamp
        self.end_date_timestamp: time = end_date_timestamp
        self.round_count: int = round_count
        self.rounds: list[Round] = rounds
        self.players: list[Player] = players
        self.time_method: TimeMethod = time_method
        self.description: str = description
