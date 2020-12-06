from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, Union
from kview.view.view import View
from kview.data_model.data_model import DataModel
from chess.validation.is_only_one_char_validator import IsOnlyOneCharValidator
from chess.validation.could_be_number_validator import CouldBeNumberValidator


class Menu(View):
    def __init__(self, model: DataModel):
        super(Menu, self).__init__(model)

    def generate(self, model: DataModel) -> str:
        view: str = HeaderPartialView.generate()
        view += TitlePartialView.generate("Gestion des tounois")
        view += ActionPartialView.generate(["Retour"])
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer (ex: '1' pour gérer les tournois)")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Union[str, None]:
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            return "/"
