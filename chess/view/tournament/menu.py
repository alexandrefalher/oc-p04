from kview.request.request import Request
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, List
from kview.view.view import View
from kview.data_model.data_model import DataModel
from chess.validation.is_only_one_char_validator import IsOnlyOneCharValidator
from chess.validation.could_be_number_validator import CouldBeNumberValidator


class Menu(View):
    def __init__(self, model: DataModel):
        super(Menu, self).__init__(model)

    def generate(self, model: DataModel) -> str:
        is_unfinished_tournament: bool = model.get("unfinished")
        actions: List[str] = []
        if is_unfinished_tournament:
            actions.append("Continuer le tournois")
        else:
            actions.append("Nouveau tournois")
        actions.append("Lister")
        actions.append("Retour")
        view: str = HeaderPartialView.generate()
        view += TitlePartialView.generate("Gestion des tounois")
        view += ActionPartialView.generate(actions)
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer (ex: '1' pour gérer les tournois)")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            is_unfinished_tournament: bool = model.get("unfinished")
            if is_unfinished_tournament:
                return Request("/tournament/continue", self.__module__, None)
            else:
                return Request("/tournament/new", self.__module__, None)
        elif user_input == "2":
            return Request("/tournament/list", self.__module__, None)
        elif user_input == "3":
            return Request("/", self.__module__, None)
        else:
            return None
