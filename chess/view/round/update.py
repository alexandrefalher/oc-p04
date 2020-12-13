from typing import List
from chess.model.entities.player import Player
from chess.model.entities.match import Match
from chess.model.entities.round import Round
from kview.request.request import Request
from chess.validation.could_be_number_validator import CouldBeNumberValidator
from chess.validation.is_only_one_char_validator import IsOnlyOneCharValidator
from chess.validation.not_none_validator import NotNoneValidator
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from kview.view.view import View
from kview.data_model.data_model import DataModel
from chess.utils.utils import Utils


class Update(View):
    def __init__(self, model: DataModel):
        super(Update, self).__init__(model)
        self.__round: Round = model.get("round")
        self.__matchs: List[Match] = model.get("matchs")
        self.__players: List[Player] = model.get("players")
        self.__tournament_id: int = model.get("tournament_id")

    def generate(self, model: DataModel) -> str:
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Modifier le joueur")
        view += "{0}: {1}\n".format("Nom", self.__round.name)
        view += "{0}: {1}\n".format("Date de début", Utils.date_to_datetime_str(self.__round.start_date_timestamp))
        view += "{0}: {1}\n".format("Date de fin", Utils.date_to_datetime_str(self.__round.end_date_timestamp))
        view += "{0}: {1}\n".format("Est terminé", self.__round.over)
        for match_id in self.__round.matchs:
            match: Match = Utils.find(self.__matchs, lambda match: match.id == match_id)
            player1: Player = Utils.find(self.__players, lambda p: p.id == match.results[0][0])
            player2: Player = Utils.find(self.__players, lambda p: p.id == match.results[1][0])
            view += "{0} > {1} : {2} < {3}\n".format(player1.firstname + player1.lastname, match.results[0][1], match.results[1][1], player2.firstname + player2.lastname)
        view += "\n"
        view += ActionPartialView.generate(["Modifier nom", "Modifier les résultats du match 1", "Modifier les résultats du match 2", "Modifier les résultats du match 3", "Modifier les résultats du match 4", "Terminer la ronde", "Retour"])
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer")
        return view

    def flow(self, user_input: str, model: DataModel) -> Request:
        if not NotNoneValidator.check(user_input):
            return None
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            self.__round.name = input("Nouveau nom >>> ")
            return Request("/round/update", self.__module__, {"round": self.__round, "tournament_id": self.__tournament_id})
        elif user_input == "2" or user_input == "3" or user_input == "4" or user_input == "5":
            player1_score: int = input("Nouveau score du joueur 1 >>> ")
            player2_score: int = input("Nouveau score du joueur 2 >>> ")
            match: Match = self.__matchs[int(user_input) - 2]
            match.results[0][1] = int(player1_score)
            match.results[1][1] = int(player2_score)
            return Request("/round/updatematch", self.__module__, {"round": self.__round, "match": match, "tournament_id": self.__tournament_id})
        elif user_input == "6":
            return Request("/round/terminate", self.__module__, self.__round)
        elif user_input == "7":
            return Request("/tournament/details", self.__module__, self.__tournament_id)
        else:
            return None
