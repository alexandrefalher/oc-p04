from chess.model.database.context import Context
from kview.controller.controller import Controller
from kview.data_model.data_model import DataModel
from kview.response.response import Response


class TournamentController(Controller):
    def __init__(self, context: Context):
        super(TournamentController, self).__init__(context)

    def menu(self, model: DataModel) -> Response:
        return Response("Menu", self.__module__, self.__class__.__name__, model)
