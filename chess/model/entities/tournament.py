from __future__ import annotations
from typing import Dict, List
import time

from chess.model.entities.entity import Entity


class Tournament(Entity):
    def __init__(self, id: int, name: str, location: str, start_date: time, end_date: time, over: bool, round_count: int, rounds: List[int], players: List[int], time_method: int, description: str):
        self.id: int = id
        self.name: str = name
        self.location: str = location
        self.start_date: time = start_date
        self.end_date: time = end_date
        self.over: bool = over
        self.round_count: int = round_count
        self.rounds: List[int] = rounds
        self.players: List[int] = players
        self.time_method: int = time_method
        self.description: str = description

    @staticmethod
    def serialize(tournament: Tournament) -> Dict:
        return {
            "id": tournament.id,
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "over": tournament.over,
            "round_count": tournament.round_count,
            "rounds": tournament.rounds,
            "players": tournament.players,
            "time_method": tournament.time_method,
            "description": tournament.description
        }

    @staticmethod
    def deserialize(serialized_entity: Dict) -> Tournament:
        return Tournament(
            serialized_entity["id"],
            serialized_entity["name"],
            serialized_entity["location"],
            serialized_entity["start_date"],
            serialized_entity["end_date"],
            serialized_entity["over"],
            serialized_entity["round_count"],
            serialized_entity["rounds"],
            serialized_entity["players"],
            serialized_entity["time_method"],
            serialized_entity["description"]
        )
