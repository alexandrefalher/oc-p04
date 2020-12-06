from __future__ import annotations
from typing import Dict
from chess.model.entities.entity import Entity


class TimeMethod(Entity):
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name

    @staticmethod
    def serialize(time_method: TimeMethod) -> Dict:
        return {
            "id": time_method.id,
            "name": time_method.name
        }

    @staticmethod
    def deserialize(serialized_entity: Dict) -> TimeMethod:
        return TimeMethod(
            id=serialized_entity["id"],
            name=serialized_entity["name"]
        )
