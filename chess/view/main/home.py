from kview.request.request import Request
from kview.data_model.data_model import DataModel
from kview.partial_view.partial_view import PartialView
from kview.view.view import View


class Home(View):
    def __init__(self, model: DataModel):
        super(Home, self).__init__("Home", model)

    def generate(self) -> str:

    def render(self) -> Request:
        return Request("/main/other", "home", DataModel({"from_view": "to_controller"}))
