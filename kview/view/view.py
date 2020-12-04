from os import system, name

from ..request.request import Request
from ..data_model.data_model import DataModel


class View:
    def __init__(self, model: DataModel):
        self.__endpoint: str = None
        self.__model: DataModel = model
        self.__source: str = self.__module__
        self.__page_content: str = None

    def generate(self, model: DataModel) -> str:
        raise NotImplementedError()

    def interact(self) -> str:
        raise NotImplementedError()

    def execute(self) -> Request:
        self.__page_content = self.generate(self.__model)
        self._render()
        self.__endpoint = self.interact()
        return Request(self.__endpoint, self.__source, self.__model)

    def _render(self) -> None:
        self._clear_console()
        print(self.__page_content)

    def _clear_console(self) -> None:
        if name == "posix":
            system("clear")
        else:
            system("cls")
