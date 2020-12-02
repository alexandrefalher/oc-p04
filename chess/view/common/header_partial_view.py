from lib.partial_view.partial_view import PartialView


class HeaderPartialView(PartialView):
    def __init__(self):
        pass

    def generate(self) -> str:
        return "-------------------------------------"\
               "     Chess tournament manager        "\
               "-------------------------------------"
