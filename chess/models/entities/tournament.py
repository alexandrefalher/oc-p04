from typing import Dict, List
from chess.models.entities.entity import Entity
import time


class Tournament(Entity):
    def __init__(self, id: int, name: str, location: str, start_date_timestamp: time, end_date_timestamp: time, round_count: int, rounds: List[int], players: List[int], time_method: int, description: str):
        self.id: int = id
        self.name: str = name
        self.location: str = location
        self.start_date_timestamp: time = start_date_timestamp
        self.end_date_timestamp: time = end_date_timestamp
        self.round_count: int = round_count
        self.rounds: List[int] = rounds
        self.players: List[int] = players
        self.time_method: int = time_method
        self.description: str = description

    def serialize(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date_timestamp": self.start_date_timestamp,
            "end_date_timesteamp": self.end_date_timestamp,
            "round_count": self.round_count,
            "rounds": "[]",
            "players": "[]",
            "time_method": self.time_method,
            "description": self.description
        }
