from chess.controllers.controller import Controller
from chess.viewmodel.choice import Choice
from chess.viewmodel.view_model import ViewModel


class MainController(Controller):
    def __init__(self):
        super(MainController, self).__init__()

    def main_page(self):
        choices: ViewModel = ViewModel("Home", [
            Choice("1", "New tournament / Continue tournament", self.main_page),
            Choice("2", "List tournaments", self.main_page),
            Choice("3", "List players", self.main_page),
            Choice("4", "Exit", lambda: None)
        ])
        self.navigate(choices)
