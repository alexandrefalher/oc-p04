from chess.view.common.input_partial_view import InputPartialView
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from kview.data_model.data_model import DataModel
from kview.view.view import View


class Home(View):
    def __init__(self, model: DataModel):
        super(Home, self).__init__(model)

    def generate(self, model: DataModel) -> str:
        view: str = HeaderPartialView.generate()
        view += TitlePartialView.generate("Home")
        view += ActionPartialView.generate(["Gestion des tournois", "Gestion des joueurs", "Quitter"])
        view += ErrorPatialView.generate(model)
        view += InputPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer (ex: '1' pour gérer les tournois)")
        return view

    def interact(self) -> str:
        user_input: str = input(">>> ")
        return user_input
