from typing import Tuple


class Match:
    def __init__(self, id: int, results: Tuple[str, str]):
        self.id: int = id
        self.results: Tuple[str, str] = results
