from lib.data_model.data_model import DataModel
from lib.partial_view.partial_view import PartialView


class ListPartialView(PartialView):
    def __init__(self):
        pass

    def generate(self, data_model: DataModel) -> str:
        generated_partial_view: str = ""
        for key, value in data_model:
            generated_partial_view += "{0} - {1}".format(key, value) + "\n"
        return generated_partial_view
