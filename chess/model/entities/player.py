from __future__ import annotations
from typing import Dict
import time

from chess.model.entities.entity import Entity


class Player(Entity):
    def __init__(self, id: int, lastname: str, firstname: str, birth_date_timestamp: time, gender_id: int, ranking: int):
        self.id: int = id
        self.lastname: str = lastname
        self.firstname: str = firstname
        self.birth_date_timestamp: time = birth_date_timestamp
        self.gender_id: int = gender_id
        self.ranking: int = ranking

    @staticmethod
    def serialize(player: Player) -> Dict:
        return {
            "id": player.id,
            "lastname": player.lastname,
            "firstname": player.firstname,
            "birth_date_timestamp": player.birth_date_timestamp,
            "gender_id": player.gender_id,
            "ranking": player.ranking
        }

    @staticmethod
    def deserialize(serialized_entity: Dict) -> Player:
        return Player(
            serialized_entity["id"],
            serialized_entity["lastname"],
            serialized_entity["firstname"],
            serialized_entity["birth_date_timestamp"],
            serialized_entity["gender_id"],
            serialized_entity["ranking"]
        )
