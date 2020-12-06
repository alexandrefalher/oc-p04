from __future__ import annotations
from typing import Dict
from chess.model.entities.entity import Entity


class Gender(Entity):
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name

    @staticmethod
    def serialize(gender: Gender) -> Dict:
        return {
            "id": gender.id,
            "name": gender.name
        }

    @staticmethod
    def deserialize(serialized_entity: Dict) -> Entity:
        return Gender(
            serialized_entity["id"],
            serialized_entity["name"]
        )
