from os import system, name

from ..request.request import Request
from ..data_model.data_model import DataModel
from ..partial_view.partial_view import PartialView


class View:
    def __init__(self, page_name: str, model: DataModel):
        self.page_name: str = page_name
        self.__model: DataModel = model
        self.__page_content: str = ""

    def render(self) -> Request:
        self.clear_console()
        print(self.__page_content)
        return Request("", "", DataModel(None))

    def generate(self, header_partial_view: PartialView, content_partial_view: PartialView, actions_partial_view: PartialView, instructions_partial_view: PartialView, input_partial_view: PartialView) -> str:
        self.__page_content += header_partial_view.generate()
        self.__page_content += "\n"
        self.__page_content += self.page_name
        self.__page_content += "\n"
        if content_partial_view is not None:
            self.__page_content += content_partial_view.generate(self.__model)
            self.__page_content += "\n"
        self.__page_content += actions_partial_view.generate()
        self.__page_content += "\n"
        self.__page_content += "\n".join([error for error in self.__model.get("errors")])
        self.__page_content += "\n"
        self.__page_content += instructions_partial_view.generate()
        self.__page_content += "\n"
        self.__page_content += input_partial_view.generate()

    def clear_console(self) -> None:
        if name == "posix":
            system("clear")
        else:
            system("cls")
