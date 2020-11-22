from typing import List
from chess.viewmodel.choice import Choice


class ChoiceViewModel:
    def __init__(self, choices: List[Choice]):
        self.choices: List[Choice] = choices
