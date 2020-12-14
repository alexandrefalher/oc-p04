from chess.model.entities.match import Match
from chess.model.entities.round import Round
from chess.model.entities.player import Player
from chess.model.entities.time_method import TimeMethod
from typing import Any, Dict, List
from chess.model.entities.tournament import Tournament
from chess.model.database.context import Context
from kview.controller.controller import Controller
from kview.data_model.data_model import DataModel
from kview.response.response import Response
from chess.model.entity_managers.tournament_manager import TournamentManager
from chess.model.entity_managers.time_method_manager import TimeMethodManager
from chess.model.entity_managers.player_manager import PlayerManager
from chess.model.entity_managers.round_manager import RoundManager
from chess.model.entity_managers.match_manager import MatchManager
from chess.model.entity_managers.gender_manager import GenderManager


class ReportController(Controller):
    def __init__(self, context: Context):
        super(ReportController, self).__init__(context)
        self.__tournament_manager: TournamentManager = TournamentManager(context)
        self.__time_method_manager: TimeMethodManager = TimeMethodManager(context)
        self.__player_manager: PlayerManager = PlayerManager(context)
        self.__round_manager: RoundManager = RoundManager(context)
        self.__match_manager: MatchManager = MatchManager(context)
        self.__gender_manager: GenderManager = GenderManager(context)

    def menu(self) -> Response:
        return Response("menu", self.__module__, self.__class__.__name__, DataModel(None))

    def get_players_by_alphabet(self) -> Response:
        players: List[Player] = self.__player_manager.get_sorted(lambda p: p.lastname)
        model: DataModel = DataModel({"players": players})
        return Response("players", self.__module__, self.__class__.__name__, model)

    def get_players_by_rank(self) -> Response:
        players: List[Player] = self.__player_manager.get_sorted(lambda p: p.ranking)
        model: DataModel = DataModel({"players": players})
        return Response("players", self.__module__, self.__class__.__name__, model)
