import time


class Round:
    def __ini__(self, id: int, matchs: list[int], start_date_timestamp: time, end_date_timestamp: time):
        self.id: int = id
        self.matchs: list[int] = matchs
        self.start_date_timestamp: time = start_date_timestamp
        self.end_date_timestamp: time = end_date_timestamp
