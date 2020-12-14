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
        players: List[Player] = self.__player_manager.get_sorted(self.__player_manager.get_all(), lambda p: p.lastname)
        model: DataModel = DataModel({"players": players})
        return Response("players", self.__module__, self.__class__.__name__, model)

    def get_players_by_rank(self) -> Response:
        players: List[Player] = self.__player_manager.get_sorted(self.__player_manager.get_all(), lambda p: p.ranking)
        model: DataModel = DataModel({"players": players})
        return Response("players", self.__module__, self.__class__.__name__, model)

    def get_tournaments(self) -> Response:
        tournaments: List[Tournament] = self.__tournament_manager.get_all_finished()
        model: DataModel = DataModel({"tournaments": tournaments})
        return Response("tournaments", self.__module__, self.__class__.__name__, model)

    def get_tournament(self, tournament_id: int) -> Response:
        tournament: Tournament = self.__tournament_manager.get(tournament_id)
        players: List[Player] = self.__player_manager.get_all()
        time_methods: List[TimeMethod] = self.__time_method_manager.get_all()
        model: DataModel = DataModel({"tournament": tournament, "players": players, "time_methods": time_methods})
        return Response("tournamentdetails", self.__module__, self.__class__.__name__, model)

    def get_tournament_players_by_alphabet(self, tournament_id: int) -> Response:
        tournament: Tournament = self.__tournament_manager.get(tournament_id)
        tournament_players: List[Player] = self.__player_manager.get_several(tournament.players)
        players_sorted: List[Player] = self.__player_manager.get_sorted(tournament_players, lambda p: p.lastname)
        model: DataModel = DataModel({"players": players_sorted, "endpoint": "/report/tournamentdetails", "data": tournament_id})
        return Response("players", self.__module__, self.__class__.__name__, model)

    def get_tournament_players_by_rank(self, tournament_id: int) -> Response:
        tournament: Tournament = self.__tournament_manager.get(tournament_id)
        tournament_players: List[Player] = self.__player_manager.get_several(tournament.players)
        players_sorted: List[Player] = self.__player_manager.get_sorted(tournament_players, lambda p: p.ranking)
        model: DataModel = DataModel({"players": players_sorted, "endpoint": "/report/tournamentdetails", "data": tournament_id})
        return Response("players", self.__module__, self.__class__.__name__, model)

    def tournament_rounds(self, tournament_id: int) -> Response:
        rounds: List[Round] = self.__round_manager.get_all_from_tournament(tournament_id)
        model: DataModel = DataModel({"tournament_id": tournament_id, "rounds": rounds})
        return Response("rounds", self.__module__, self.__class__.__name__, model)

    def tournament_matchs(self, tournament_id: int) -> Response:
        matchs: List[Match] = self.__match_manager.get_all_from_tournament(tournament_id)
        players: List[Player] = self.__player_manager.get_all()
        model: DataModel = DataModel({"tournament_id": tournament_id, "matchs": matchs, "players": players})
        return Response("matchs", self.__module__, self.__class__.__name__, model)
