import time
from typing import List


class Round:
    def __ini__(self, id: int, matchs: List[int], start_date_timestamp: time, end_date_timestamp: time):
        self.id: int = id
        self.matchs: List[int] = matchs
        self.start_date_timestamp: time = start_date_timestamp
        self.end_date_timestamp: time = end_date_timestamp
