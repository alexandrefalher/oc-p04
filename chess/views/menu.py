from chess.viewmodel.choice import Choice
from chess.viewmodel.choice_view_model import ChoiceViewModel
from chess.views.view import View


class Menu(View):
    def __init__(self, choices: ChoiceViewModel):
        super()
        self.__viewmodel: ChoiceViewModel = choices

    def generate(self) -> str:
        result: str = ""
        return result.join([self.__generate_line(choice) for choice in self.__viewmodel.choices])

    def __generate_line(self, choice: Choice) -> str:
        return choice.id + " - " + choice.description + "\n"
