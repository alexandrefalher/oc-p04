from lib.request.request import Request
from lib.data_model.data_model import DataModel
from lib.partial_view.partial_view import PartialView
from lib.view.view import View


class Home(View):
    def __init__(self, model: DataModel):
        super(Home, self).__init__("Home", model)

    def generate(self) -> str:
        header_partial_view: PartialView = None
        content_partial_view: PartialView = None
        actions_partial_view: PartialView = None
        instructions_partial_view: PartialView = None
        input_partial_view: PartialView = None
        super(Home, self).generate(header_partial_view, content_partial_view, actions_partial_view, instructions_partial_view, input_partial_view)

    def render(self) -> Request:
        return Request("/main/other", "home", DataModel({"from_view": "to_controller"}))
