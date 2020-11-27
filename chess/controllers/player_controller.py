from chess.models.entities.player import Player
from typing import List
from chess.viewmodel.choice import Choice
from chess.viewmodel.view_model import ViewModel
from chess.controllers.controller import Controller
from chess.config import Config
from chess.models.entity_managers.player_manager import PlayerManager


class PlayerController(Controller):
    def __init__(self, config: Config):
        super(PlayerController, self).__init__(config)
        self.__player_manager: PlayerManager = PlayerManager(self._context)

    def main(self) -> None:
        choices: ViewModel = ViewModel("Player management", [
            Choice("1", "List players", None)
        ])
        self.navigate(choices)

    def list(self) -> None:
        players: List[Player] = self.__player_manager.get_all()
        choices: ViewModel = ViewModel("Player management - player list", [])
        for i, player in enumerate(players):
            choices.add_choice(Choice(i, "{0} {1} -> {2}".format(player.firstname, player.lastname, player.ranking), None))
        self.navigate(choices)
