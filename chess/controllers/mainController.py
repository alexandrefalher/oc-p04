from chess.viewmodel.choice import Choice
from chess.views.view_builder import ViewBuilder
from chess.views.menu import Menu
from chess.viewmodel.choice_view_model import ChoiceViewModel


class MainController:
    def __init__(self):
        self.__view_builder: ViewBuilder = ViewBuilder()

    def main_page(self):
        choices: ChoiceViewModel = ChoiceViewModel([
            Choice("1", "New tournament / Continue tournament", self.main_page),
            Choice("2", "List tournaments", self.main_page),
            Choice("3", "List players", self.main_page)
        ])

        self.__view_builder.add_view(Menu(choices))
        self.__view_builder.render()

        choice: str = input()
        choices[choice][1]()
