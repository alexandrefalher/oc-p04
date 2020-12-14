from chess.model.entities.player import Player
from kview.request.request import Request
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, List
from kview.view.view import View
from kview.data_model.data_model import DataModel
import time


class Players(View):
    def __init__(self, model: DataModel):
        super(Players, self).__init__(model)
        self.__players: List[Player] = model.get("players")

    def generate(self, model: DataModel) -> str:
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Liste des joueurs")
        for player in self.__players:
            bd_local = time.localtime(player.birth_date)
            birth_date = "{0}/{1}/{2}".format(bd_local.tm_mday, bd_local.tm_mon, bd_local.tm_year)
            view += "{0} {1} {2} {3}\n".format(player.ranking, player.lastname, player.firstname, birth_date)
        view += "\n"
        view += ActionPartialView.generate(["Retour"])
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if user_input == "1":
            return Request("/report/menu", self.__module__, None)
        else:
            return None
