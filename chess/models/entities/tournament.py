from __future__ import annotations
from typing import Dict, List
from chess.models.entities.entity import Entity
import time


class Tournament(Entity):
    def __init__(self, id: int, name: str, location: str, start_date_timestamp: time, end_date_timestamp: time, over: bool, round_count: int, rounds: List[int], players: List[int], time_method: int, description: str):
        self.id: int = id
        self.name: str = name
        self.location: str = location
        self.start_date_timestamp: time = start_date_timestamp
        self.end_date_timestamp: time = end_date_timestamp
        self.over: bool = over
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
            "over": self.over,
            "round_count": self.round_count,
            "rounds": "[]",
            "players": "[]",
            "time_method": self.time_method,
            "description": self.description
        }

    @classmethod
    def deserialize(cls, serialized_entity: Dict):
        return cls(
            serialized_entity["id"],
            serialized_entity["name"],
            serialized_entity["location"],
            serialized_entity["start_date_timestamp"],
            serialized_entity["end_date_timestamp"],
            serialized_entity["over"],
            serialized_entity["round_count"],
            serialized_entity["rounds"],
            serialized_entity["players"],
            serialized_entity["time_method"],
            serialized_entity["description"]
        )
