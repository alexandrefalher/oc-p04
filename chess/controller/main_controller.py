from kview.response.response import Response
from kview.data_model.data_model import DataModel


class MainController:
    def __init__(self):
        pass

    def get(self, model: DataModel) -> Response:
        model.add("new_key", "new_value")
        return Response("Home", self.__module__, self.__class__.__name__, model)
