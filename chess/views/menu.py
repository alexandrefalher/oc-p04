from chess.viewmodel.view_model import ViewModel
from chess.views.list import List
from chess.viewmodel.choice import Choice
from chess.views.view import View


class Menu(View):
    def __init__(self, viewmodel: ViewModel):
        super()
        self.__viewmodel: ViewModel = viewmodel

    def generate(self) -> str:
        result: List[str] = []
        error: str = self.__viewmodel.error
        result.append(self.__viewmodel.title + "\n\n")
        for choice in self.__viewmodel.choices:
            result.append(self.__generate_line(choice))
        if error != "":
            result.append("\n" + error + "\n")
        return "".join(result)

    def __generate_line(self, choice: Choice) -> str:
        return choice.id + " - " + choice.description + "\n"
