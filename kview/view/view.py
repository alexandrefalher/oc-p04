from os import system, name
from typing import Any

from ..request.request import Request
from ..data_model.data_model import DataModel
from ..utils.console import Console


class View:
    def __init__(self, model: DataModel):
        self.__model: DataModel = model
        self.__page_content: str = None

    def generate(self, model: DataModel) -> str:
        raise NotImplementedError()

    def flow(self, user_input: Any, mode: DataModel) -> Request:
        raise NotImplementedError()

    def execute(self) -> Request:
        while True:
            self.__page_content = self.generate(self.__model)
            self._render()
            user_input: str = input(">>> ")
            request: Request = self.flow(user_input, self.__model)
            if request is not None:
                break
        return request

    def _render(self) -> None:
        Console.clear_console()
        print(self.__page_content)
