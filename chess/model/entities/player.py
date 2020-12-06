from __future__ import annotations
from typing import Dict
import time

from chess.model.entities.entity import Entity


class Player(Entity):
    def __init__(self, id: int, lastname: str, firstname: str, birth_date: time, gender: int, ranking: int):
        self.id: int = id
        self.lastname: str = lastname
        self.firstname: str = firstname
        self.birth_date: time = birth_date
        self.gender: int = gender
        self.ranking: int = ranking

    @staticmethod
    def serialize(player: Player) -> Dict:
        return {
            "id": player.id,
            "lastname": player.lastname,
            "firstname": player.firstname,
            "birth_date": player.birth_date,
            "gender": player.gender,
            "ranking": player.ranking
        }

    @staticmethod
    def deserialize(serialized_entity: Dict) -> Player:
        return Player(
            serialized_entity["id"],
            serialized_entity["lastname"],
            serialized_entity["firstname"],
            serialized_entity["birth_date"],
            serialized_entity["gender"],
            serialized_entity["ranking"]
        )
