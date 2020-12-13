from __future__ import annotations
from chess.model.entities.entity import Entity
import time
from typing import Dict, List


class Round(Entity):
    def __init__(self, id: int, name: str, matchs: List[int], start_date_timestamp: time, end_date_timestamp: time, over: bool):
        self.id: int = id
        self.name: str = name
        self.matchs: List[int] = matchs
        self.start_date_timestamp: time = start_date_timestamp
        self.end_date_timestamp: time = end_date_timestamp
        self.over: bool = over

    @staticmethod
    def serialize(round: Round) -> Dict:
        return {
            "id": round.id,
            "name": round.name,
            "matchs": round.matchs,
            "start_date_timestamp": round.start_date_timestamp,
            "end_date_timestamp": round.end_date_timestamp,
            "over": round.over
        }

    @staticmethod
    def deserialize(serialized_entity: Dict) -> Round:
        return Round(
            id=serialized_entity["id"],
            name=serialized_entity["name"],
            matchs=serialized_entity["matchs"],
            start_date_timestamp=serialized_entity["start_date_timestamp"],
            end_date_timestamp=serialized_entity["end_date_timestamp"],
            over=serialized_entity["over"]
        )
