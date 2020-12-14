from chess.model.entities.time_method import TimeMethod
from chess.model.entities.tournament import Tournament
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
from chess.model.entities.player import Player


class Tournamentdetails(View):
    def __init__(self, model: DataModel):
        super(Tournamentdetails, self).__init__(model)
        self.__tournament: Tournament = model.get("tournament")
        self.__players: List[Player] = model.get("players")
        self.__time_methods: List[TimeMethod] = model.get("time_methods")

    def generate(self, model: DataModel) -> str:
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Détails du tournois")
        view += "{0}: {1}\n".format("Nom", self.__tournament.name)
        view += "{0}: {1}\n".format("Lieu", self.__tournament.location)
        view += "{0}: {1}\n".format("Date de début", Utils.date_to_date_str(self.__tournament.start_date))
        view += "{0}: {1}\n".format("Date de fin", Utils.date_to_date_str(self.__tournament.end_date))
        view += "{0}: {1}\n".format("Description", self.__tournament.description)
        time_method: TimeMethod = Utils.find(self.__time_methods, lambda tm: tm.id == self.__tournament.time_method)
        view += "{0}: {1}\n".format("Gestion du temps", time_method.name)
        for player_id in self.__tournament.players:
            player: Player = Utils.find(self.__players, lambda player: player.id == player_id)
            view += "         {0} {1}, classement: {2}\n".format(player.firstname, player.lastname, player.ranking)
        view += "{0}: {1}\n".format("Nombre de rondes", self.__tournament.round_count)
        view += "{0}: {1}\n".format("Terminé", self.__tournament.over)
        view += "\n"
        view += ActionPartialView.generate([
            "Lister les joueurs par ordre alphabétique",
            "Lister les joueurs par classement",
            "Lister les rondes",
            "Lister les tours",
            "Retour"
        ])
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if not NotNoneValidator.check(user_input):
            return None
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            return Request("/report/tournamentplayersalpha", self.__module__, self.__tournament.id)
        elif user_input == "2":
            return Request("/report/tournamentplayersrank", self.__module__, self.__tournament.id)
        elif user_input == "3":
            return Request("/report/tournamentrounds", self.__module__, self.__tournament.id)
        elif user_input == "4":
            return Request("/report/tournamentmatchs", self.__module__, self.__tournament.id)
        elif user_input == "5":
            return Request("/report/tournamentlist", self.__module__, None)
        else:
            return None
