from chess.model.entities.round import Round
from chess.model.entities.player import Player
from chess.model.entities.time_method import TimeMethod
import time
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


class TournamentController(Controller):
    def __init__(self, context: Context):
        super(TournamentController, self).__init__(context)
        self.__tournament_manager: TournamentManager = TournamentManager(context)
        self.__time_method_manager: TimeMethodManager = TimeMethodManager(context)
        self.__player_manager: PlayerManager = PlayerManager(context)
        self.__round_manager: RoundManager = RoundManager(context)

    def menu(self) -> Response:
        is_unfinished_tournament: bool = self.__tournament_manager.is_unfinished_tournament()
        model: DataModel = DataModel({"unfinished": is_unfinished_tournament})
        return Response("Menu", self.__module__, self.__class__.__name__, model)

    def get(self, tournament_id: int) -> Response:
        tournament: Tournament = self.__tournament_manager.get(tournament_id)
        players: List[Player] = self.__player_manager.get_all()
        time_methods: List[TimeMethod] = self.__time_method_manager.get_all()
        model: DataModel = DataModel({"entity": tournament, "players": players, "time_methods": time_methods})
        return Response("Update", self.__module__, self.__class__.__name__, model)

    def get_all(self) -> Response:
        tournaments: List[Tournament] = self.__tournament_manager.get_all()
        model: DataModel = DataModel({"tournaments": tournaments})
        return Response("List", self.__module__, self.__class__.__name__, model)

    def create(self) -> Response:
        if self.__tournament_manager.is_unfinished_tournament():
            return Response("Menu", self.__module__, self.__class__.__name__, DataModel({"errors": "Un tournois est déjà commencé"}))
        tournament: Tournament = Tournament(0, "", "", time.mktime(time.localtime()), 0, False, 4, [0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], 0, "")
        id: int = self.__tournament_manager.create(tournament)
        tournament.id = id
        players: List[Player] = self.__player_manager.get_all()
        time_methods: List[TimeMethod] = self.__time_method_manager.get_all()
        model: DataModel = DataModel({"entity": tournament, "players": players, "time_methods": time_methods, "tournament_id": tournament.id})
        return Response("Update", self.__module__, self.__class__.__name__, model)

    def update(self, tournament: Tournament) -> Response:
        self.__tournament_manager.update(tournament.id, tournament)
        players: List[Player] = self.__player_manager.get_all()
        time_methods: List[TimeMethod] = self.__time_method_manager.get_all()
        model: DataModel = DataModel({"entity": tournament, "players": players, "time_methods": time_methods})
        return Response("Update", self.__module__, self.__class__.__name__, model)

    def continue_tournament(self) -> Response:
        tournament: Tournament = self.__tournament_manager.get_unfinished()
        players: List[Player] = self.__player_manager.get_all()
        time_methods: List[TimeMethod] = self.__time_method_manager.get_all()
        model: DataModel = DataModel({"entity": tournament, "players": players, "time_methods": time_methods})
        return Response("Update", self.__module__, self.__class__.__name__, model)

    def chooseplayer(self, tournament_id: int) -> Response:
        tournament: Tournament = self.__tournament_manager.get(tournament_id)
        players: List[Player] = self.__player_manager.get_all()
        model: DataModel = DataModel({"entity": tournament, "players": players})
        return Response("Chooseplayer", self.__module__, self.__class__.__name__, model)

    def searchplayer(self, args: Dict[str, Any]) -> Response:
        tournament: Tournament = self.__tournament_manager.get(args["tournament_id"])
        tournament_player_index: int = args["tournament_player_index"]
        players: List[Player] = self.__player_manager.get_all()
        model: DataModel = DataModel({"tournament": tournament, "players": players, "tournament_player_index": tournament_player_index})
        return Response("Searchplayer", self.__module__, self.__class__.__name__, model)

    def choosetimemethod(self, tournament_id: int) -> Response:
        tournament: Tournament = self.__tournament_manager.get(tournament_id)
        time_methods: List[TimeMethod] = self.__time_method_manager.get_all()
        model: DataModel = DataModel({"tournament": tournament, "time_methods": time_methods})
        return Response("choosetimemethod", self.__module__, self.__class__.__name__, model)

    def chooseround(self, tournament_id: int) -> Response:
        tournament: Tournament = self.__tournament_manager.get(tournament_id)
        rounds: List[Round] = self.__round_manager.get_all()
        model: DataModel = DataModel({"tournament": tournament, "rounds": rounds})
        return Response("chooseround", self.__module__, self.__class__.__name__, model)
