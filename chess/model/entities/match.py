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
            "p1": entity.results[0][0],
            "r1": entity.results[0][1],
            "p2": entity.results[1][0],
            "r2": entity.results[1][1]
        }

    @staticmethod
    def deserialize(serialized_entity: Dict) -> Match:
        return Match(
            id=serialized_entity["id"],
            results=([int(serialized_entity["p1"]), int(serialized_entity["r1"])], [int(serialized_entity["p2"]), int(serialized_entity["r2"])])
        )
