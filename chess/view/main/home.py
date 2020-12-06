from kview.request.request import Request
from chess.validation.could_be_number_validator import CouldBeNumberValidator
from chess.validation.is_only_one_char_validator import IsOnlyOneCharValidator
from typing import Any
from chess.view.common.instruction_partial_view import InstructionPartialView
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from kview.data_model.data_model import DataModel
from kview.view.view import View


class Home(View):
    def __init__(self, model: DataModel):
        super(Home, self).__init__(model)

    def generate(self, model: DataModel) -> str:
        view: str = HeaderPartialView.generate()
        view += TitlePartialView.generate("Home")
        view += ActionPartialView.generate(["Gestion des tournois", "Gestion des joueurs", "Quitter"])
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer (ex: '1' pour gérer les tournois)")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            return Request("/tournament/menu", self.__module__, None)
        elif user_input == "2":
            return Request("/player/menu", self.__module__, None)
        elif user_input == "3":
            return Request("/exit", self.__module__, None)
        else:
            return None
