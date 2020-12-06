from chess.model.entities.gender import Gender
from chess.model.entity_managers.gender_manager import GenderManager
from chess.model.database.context import Context
from typing import List
from chess.model.entities.player import Player
from chess.model.entity_managers.player_manager import PlayerManager
from kview.controller.controller import Controller
from kview.response.response import Response
from kview.data_model.data_model import DataModel


class PlayerController(Controller):
    def __init__(self, context: Context):
        super(PlayerController, self).__init__(context)
        self.__player_manager: PlayerManager = PlayerManager(self._context)
        self.__gender_manager: GenderManager = GenderManager(self._context)

    def menu(self) -> Response:
        model: DataModel = DataModel(None)
        return Response("Menu", self.__module__, self.__class__.__name__, model)

    def get_all(self) -> Response:
        players: List[Player] = self.__player_manager.get_all()
        model = DataModel({"entities": players})
        return Response("list", self.__module__, self.__class__.__name__, model)

    def get(self, id: int) -> Response:
        player: Player = self.__player_manager.get(id)
        genders: List[Gender] = self.__gender_manager.get_all()
        model = DataModel({"entity": player, "genders": genders})
        return Response("details", self.__module__, self.__class__.__name__, model)

    def to_create(self) -> Response:
        genders: List[Gender] = self.__gender_manager.get_all()
        model: DataModel = DataModel({"entity": Player(0, "", "", "", 0, 0), "genders": genders})
        return Response("create", self.__module__, self.__class__.__name__, model)

    def create(self, player: Player) -> Response:
        player_id: int = self.__player_manager.create(player)
        player.id = player_id
        genders: List[Gender] = self.__gender_manager.get_all()
        model: DataModel = DataModel({"entity": player, "genders": genders})
        return Response("details", self.__module__, self.__class__.__name__, model)

    def to_update(self, id: int) -> Response:
        player: Player = self.__player_manager.get(id)
        genders: List[Gender] = self.__gender_manager.get_all()
        model: DataModel = DataModel({"entity": player, "genders": genders})
        return Response("update", self.__module__, self.__class__.__name__, model)

    def update(self, player: Player) -> Response:
        self.__player_manager.update(player.id, player)
        genders: List[Gender] = self.__gender_manager.get_all()
        model: DataModel = DataModel({"entity": player, "genders": genders})
        return Response("details", self.__module__, self.__class__.__name__, model)
