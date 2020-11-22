from chess.views.list import List
from chess.viewmodel.choice import Choice


class ViewModel:
    def __init__(self, choices: List[Choice]):
        self.choices: List[Choice] = choices
