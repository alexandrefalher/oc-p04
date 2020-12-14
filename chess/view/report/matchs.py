from chess.model.entities.player import Player
from chess.model.entities.match import Match
from kview.request.request import Request
from chess.validation.could_be_number_validator import CouldBeNumberValidator
from chess.validation.is_only_one_char_validator import IsOnlyOneCharValidator
from chess.validation.not_none_validator import NotNoneValidator
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, List
from kview.view.view import View
from kview.data_model.data_model import DataModel
from chess.utils.utils import Utils


class Matchs(View):
    def __init__(self, model: DataModel):
        super(Matchs, self).__init__(model)
        self.__tournament_id: int = model.get("tournament_id")
        self.__matchs: List[Match] = model.get("matchs")
        self.__players: List[Player] = model.get("players")

    def generate(self, model: DataModel) -> str:
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Liste des matchs")
        for match in self.__matchs:
            player1: Player = Utils.find(self.__players, lambda p: p.id == match.results[0][0])
            player2: Player = Utils.find(self.__players, lambda p: p.id == match.results[1][0])
            view += "{0} {1} > {2} : {3} < {4} {5}\n".format(player1.firstname, player1.lastname, match.results[0][1], match.results[1][1], player2.firstname, player2.lastname)
        view += "\n"
        view += ActionPartialView.generate(["Retour"])
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro de l'action que vous voulez exécuter")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if not NotNoneValidator.check(user_input):
            return None
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            return Request("/report/tournamentdetails", self.__module__, self.__tournament_id)
        else:
            return None
