from chess.views.view_builder import ViewBuilder
from chess.views.menu import Menu


class MainController:
    def __init__(self):
        self.__view_builder: ViewBuilder = ViewBuilder()

    def main_page(self):
        choices: dict = {
            "1": ["New tournament / Continue tournament", self.main_page],
            "2": ["List tournaments", self.main_page],
            "3": ["List players", self.main_page]
        }

        self.__view_builder.add_view(Menu(choices))
        self.__view_builder.render()

        choice: str = input()
        choices[choice][1]()
