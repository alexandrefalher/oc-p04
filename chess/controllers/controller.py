from typing import Dict
from chess.config import Config
from chess.models.database.context import Context
from chess.views.menu import Menu
from chess.views.view_builder import ViewBuilder
from chess.viewmodel.view_model import ViewModel


class Controller:
    def __init__(self, config: Config):
        self.__view_builder: ViewBuilder = ViewBuilder()
        self.__view_model: ViewModel = None
        self.__user_choice: str = None
        self._context: Context = Context(config)

    def navigate(self, view_model: ViewModel, data: Dict) -> None:
        self.__view_model = view_model
        while True:
            self.__render_view()
            self.__ask_user_choice()
            callback = view_model.get_corresponding_callback(self.__user_choice)
            if callback is not None:
                break
            else:
                self.__view_model.error = "'{0}' is not a correct choice, please try again.".format(self.__user_choice)
        callback(data)

    def __ask_user_choice(self) -> None:
        self.__user_choice = input(">>> ")

    def __render_view(self) -> None:
        self.__view_builder.add_view(Menu(self.__view_model))
        self.__view_builder.render()
