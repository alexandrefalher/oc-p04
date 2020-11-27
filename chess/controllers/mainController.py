from typing import Dict
from chess.config import Config
from chess.models.entity_managers.tournament_manager import TournamentManager
from chess.controllers.controller import Controller
from chess.viewmodel.choice import Choice
from chess.viewmodel.view_model import ViewModel


class MainController(Controller):
    def __init__(self, config: Config):
        super(MainController, self).__init__(config)
        self.__tournament_manager: TournamentManager = TournamentManager(self._context)

    def main_page(self, data: Dict) -> None:
        new_tournament_or_continue_one: str = "Create new tournament"
        if self.__tournament_manager.is_unfinished_tournament():
            new_tournament_or_continue_one = "Continue tournament"

        choices: ViewModel = ViewModel("Home", [
            Choice("1", new_tournament_or_continue_one, self.main_page),
            Choice("2", "Manage tournaments", self.main_page),
            Choice("3", "Manage players", self.main_page),
            Choice("4", "Exit", lambda: None)
        ])
        self.navigate(choices, {"test": "value"})
