from chess.viewmodel.choice import Choice
from typing import List


class ViewModel:
    def __init__(self, title: str, choices: List[Choice]):
        self.title: str = title
        self.error: str = ""
        self.choices: List[Choice] = choices

    def get_corresponding_callback(self, choice_id: str) -> lambda _: None:
        for choice in self.choices:
            if choice.id == choice_id:
                return choice.callback
        return None

    def add_choice(self, choice: Choice) -> None:
        self.choices.append(choice)
