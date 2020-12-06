from __future__ import annotations
from chess.model.entities.entity import Entity
from typing import Dict, Tuple


class Match(Entity):
    def __init__(self, id: int, results: Tuple[str, str]):
        self.id: int = id
        self.results: Tuple[str, str] = results

    @staticmethod
    def serialize(entity: Match) -> Dict:
        return {
            "id": entity.id,
            "results": entity.results
        }

    @staticmethod
    def deserialize(serialized_entity: Dict) -> Match:
        return Match(
            id=serialized_entity["id"],
            results=serialized_entity["results"]
        )
