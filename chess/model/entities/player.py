from __future__ import annotations
from typing import Dict
import time

from chess.model.entities.entity import Entity
from chess.model.entities.gender import Gender


class Player(Entity):
    def __init__(self, lastname: str, firstname: str, birth_date_timestamp: time, gender: Gender, ranking: int):
        self.id: int = 0
        self.lastname: str = lastname
        self.firstname: str = firstname
        self.birth_date_timestamp: time = birth_date_timestamp
        self.gender: Gender = gender
        self.ranking: int = ranking

    def serialize(self) -> Dict:
        return {
            "id": self.id,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birth_date_timestamp": self.birth_date_timestamp,
            "gender": self.gender,
            "ranking": self.ranking
        }

    def deserialize(self, serialized_entity: Dict) -> Player:
        return Player(
            serialized_entity["id"],
            serialized_entity["lastname"],
            serialized_entity["firstname"],
            serialized_entity["birth_date_timestamp"],
            serialized_entity["gender"],
            serialized_entity["ranking"]
        )
