import time


class PlayerDto:
    def __init__(self, id: int, lastname: str, firstname: str, birth_date: time, gender_id: int, ranking: int):
        self.id: int = id
        self.lastname: str = lastname
        self.firstname: str = firstname
        self.birth_date: time = birth_date
        self.gender_id: int = gender_id
        self.ranking: int = ranking
