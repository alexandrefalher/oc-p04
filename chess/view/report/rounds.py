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
from chess.model.entities.round import Round


class Rounds(View):
    def __init__(self, model: DataModel):
        super(Rounds, self).__init__(model)
        self.__tournament_id: int = model.get("tournament_id")
        self.__rounds: List[Round] = model.get("rounds")

    def generate(self, model: DataModel) -> str:
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Liste des rondes")
        for round in self.__rounds:
            view += "{0}: {1} - {2} > {3}\n".format(round.name, Utils.date_to_datetime_str(round.start_date_timestamp), Utils.date_to_datetime_str(round.end_date_timestamp), round.over)
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
