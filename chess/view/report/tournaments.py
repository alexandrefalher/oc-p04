from chess.utils.utils import Utils
from chess.model.entities.tournament import Tournament
from kview.request.request import Request
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, List
from kview.view.view import View
from kview.data_model.data_model import DataModel


class Tournaments(View):
    def __init__(self, model: DataModel):
        super(Tournaments, self).__init__(model)
        self.__tournaments: List[Tournament] = model.get("tournaments")
        self.__actions: List[str] = []

    def generate(self, model: DataModel) -> str:
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Liste des tournois")
        for tournament in self.__tournaments:
            self.__actions.append("Voir le détail de: {0} {1} {2} {3} {4} {5}".format(tournament.name, tournament.location, Utils.date_to_datetime_str(tournament.start_date), Utils.date_to_datetime_str(tournament.end_date), tournament.round_count, tournament.over))
        self.__actions.append("Retour")
        view += "\n"
        view += ActionPartialView.generate(self.__actions)
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if int(user_input) >= 1 and int(user_input) < len(self.__actions):
            return Request("/report/tournamentdetails", self.__module__, self.__tournaments[int(user_input) - 1].id)
        elif int(user_input) == len(self.__actions):
            return Request("/report/menu", self.__module__, None)
        else:
            return None
