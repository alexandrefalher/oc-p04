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
from chess.view.utils.utils import Utils
from chess.model.entities.player import Player


class Update(View):
    def __init__(self, model: DataModel):
        super(Update, self).__init__(model)
        self.__tournament: Tournament = model.get("entity")
        self.__players: List[Player] = model.get("players")
        self.__time_methods: List[TimeMethod] = model.get("time_methods")

    def generate(self, model: DataModel) -> str:
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Modification de tournois")
        view += "{0}: {1}\n".format("Nom", self.__tournament.name)
        view += "{0}: {1}\n".format("Lieu", self.__tournament.location)
        view += "{0}: {1}\n".format("Date de début", Utils.date_time_to_str(self.__tournament.start_date))
        view += "{0}: {1}\n".format("Date de fin", Utils.date_time_to_str(self.__tournament.end_date))
        view += "{0}: {1}\n".format("Description", self.__tournament.description)
        time_method: TimeMethod = Utils.find(self.__time_methods, lambda tm: tm.id == self.__tournament.time_method)
        if time_method is not None:
            view += "{0}: {1}\n".format("Gestion du temps", time_method.name)
        else:
            view += "{0}: aucune assignée\n".format("Gestion du temps")
        view += "{0}:\n".format("Joueurs")
        for player_id in self.__tournament.players:
            player: Player = Utils.find(self.__players, lambda player: player.id == player_id)
            if player is not None:
                view += "         {0} {1}, classement: {2}\n".format(player.firstname, player.lastname, player.ranking)
        view += "{0}: {1}\n".format("Nombre de rondes", self.__tournament.round_count)
        view += "{0}: {1}\n".format("Terminé", self.__tournament.over)
        view += "\n"
        view += ActionPartialView.generate([
            "Modifier le nom",
            "Modifier le lieu",
            "Modifier la description",
            "Modifier la gestion du temps",
            "Modifier les joueurs",
            "Commencer le tournois",
            "Enregistrer",
            "Terminer nok",
            "Retour"
        ])
        view += ErrorPatialView.generate(model)
        instruction: str = model.get("instruction")
        if instruction is None:
            instruction = "Entrez le nom du tournois"
        view += InstructionPartialView.generate(instruction)
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if not NotNoneValidator.check(user_input):
            return None
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            self.__tournament.name = input("Nouveau nom >>>")
            model.update("entity", self.__tournament)
            return None
        elif user_input == "2":
            self.__tournament.location = input("Nouveau le lieu >>>")
            model.update("entity", self.__tournament)
            return None
        elif user_input == "3":
            self.__tournament.description = input("Nouvelle description >>>")
            model.update("entity", self.__tournament)
            return None
        elif user_input == "4":
            return Request("/tournament/choosetimemethod", self.__module__, self.__tournament.id)
        elif user_input == "5":
            return Request("/tournament/chooseplayer", self.__module__, self.__tournament.id)
        elif user_input == "6":
            # commencer tournois
            return None
        elif user_input == "7":
            return Request("/tournament/update", self.__module__, self.__tournament)
        elif user_input == "8":
            return Request("/tournament/terminate", self.__module__, self.__tournament.id)
        elif user_input == "9":
            return Request("/tournament/menu", self.__module__, None)
        else:
            return None
