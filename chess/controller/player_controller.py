from kview.controller.controller import Controller
from kview.response.response import Response
from kview.data_model.data_model import DataModel


class PlayerController(Controller):
    def __init__(self):
        pass

    def menu(self, model: DataModel) -> Response:
        return Response("Menu", self.__module__, self.__class__.__name__, model)
