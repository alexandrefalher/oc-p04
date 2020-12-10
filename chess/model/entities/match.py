from __future__ import annotations
from chess.model.entities.entity import Entity
from typing import Any, Dict, List, Tuple


class Match(Entity):
    def __init__(self, id: int, results: Tuple[List[Any], List[Any]]):
        self.id: int = id
        self.results: Tuple[List[Any], List[Any]] = results

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
