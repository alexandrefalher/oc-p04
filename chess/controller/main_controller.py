from kview.data_model.data_model import DataModel
from kview.controller.controller import Controller
from chess.model.database.context import Context
from kview.response.response import Response


class MainController(Controller):
    def __init__(self, context: Context):
        super(MainController, self).__init__(context)

    def menu(self) -> Response:
        model: DataModel = DataModel(None)
        return Response("Home", self.__module__, self.__class__.__name__, model)
