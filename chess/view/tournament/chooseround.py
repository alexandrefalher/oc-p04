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
from chess.model.entities.round import Round


class Chooseround(View):
    def __init__(self, model: DataModel):
        super(Chooseround, self).__init__(model)
        self.__tournament: Tournament = model.get("tournament")
        self.__rounds: List[Round] = model.get("rounds")

    def generate(self, model: DataModel) -> str:
        actions: List[str] = []
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Création de tournois - assignation des joueurs")
        round_count: int = 0
        while round_count < self.__tournament.round_count:
            if self.__tournament.rounds[round_count] != 0:
                round: Round = Utils.find(self.__rounds, lambda round: round.id == self.__tournament.rounds[round_count])
                actions.append("{0}: {1} - {2} > {3}\n".format(round.name, Utils.date_to_datetime_str(round.start_date_timestamp), Utils.date_to_datetime_str(round.end_date_timestamp), round.over))
            else:
                actions.append("Ronde non jouée\n")
            round_count += 1
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
        if 1 <= int(user_input) and int(user_input) <= self.__tournament.round_count:
            if self.__tournament.rounds[int(user_input) - 1] == 0:
                return Request("/round/create", self.__module__, {"tournament_id": self.__tournament.id, "tournament_round_index": int(user_input) - 1})
            else:
                return Request("/round/toupdate", self.__module__, {"round_id": self.__tournament.rounds[int(user_input) - 1], "tournament_id": self.__tournament.id})
        elif int(user_input) > self.__tournament.round_count:
            return Request("/tournament/update", self.__module__, self.__tournament)
        else:
            return None
