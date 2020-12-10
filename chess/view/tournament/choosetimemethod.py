from chess.model.entities.tournament import Tournament
from chess.model.entities.time_method import TimeMethod
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


class Choosetimemethod(View):
    def __init__(self, model: DataModel):
        super(Choosetimemethod, self).__init__(model)
        self.__tournament: Tournament = model.get("tournament")
        self.__time_methods: List[TimeMethod] = model.get("time_methods")

    def generate(self, model: DataModel) -> str:
        actions: List[str] = []
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Création de tournois - assignation des joueurs")
        for time_method in self.__time_methods:
            actions.append("{0}\n".format(time_method.name))
        view += "\n"
        actions.append("Retour")
        view += ActionPartialView.generate(actions)
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro de l'emplacement sur lequel vous voulez assigner un joueur")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if not NotNoneValidator.check(user_input):
            return None
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if 1 <= int(user_input) and int(user_input) <= 3:
            self.__tournament.time_method = int(user_input)
            return Request("/tournament/update", self.__module__, self.__tournament)
        elif user_input == "4":
            return Request("/tournament/update", self.__module__, self.__tournament)
        else:
            return None
