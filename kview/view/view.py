from os import system, name

from ..request.request import Request
from ..data_model.data_model import DataModel


class View:
    def __init__(self, model: DataModel):
        self._page_name: str = None
        self._endpoint: str = None
        self.__model: DataModel = model
        self.__page_content: str = None
        self.__source: str = self.__module__

    def execute(self) -> Request:
        self.__page_content = self.generate(self.__model)
        self._render()
        return Request(self._endpoint, self.__source, self.__model)

    def generate(self, model: DataModel) -> str:
        raise NotImplementedError()

    def _render(self) -> None:
        self._clear_console()
        print(self.__page_content)

    def _clear_console(self) -> None:
        if name == "posix":
            system("clear")
        else:
            system("cls")
