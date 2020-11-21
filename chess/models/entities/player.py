import time

from chess.models.entities.gender import Gender


class Player:
    def __init__(self, lastname: str, firstname: str, birth_date_timestamp: time, gender: Gender, ranking: int):
        self.id: int = 0
        self.lastname: str = lastname
        self.firstname: str = firstname
        self.birth_date_timestamp: time = birth_date_timestamp
        self.gender: Gender = gender
        self.ranking: int = ranking
