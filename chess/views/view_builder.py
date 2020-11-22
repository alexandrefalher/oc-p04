from __future__ import annotations
from typing import List
from chess.views.footer import Footer
from chess.views.header import Header
from os import system, name
from chess.views.view import View


class ViewBuilder:
    def __init__(self):
        self.__views: list[View] = []
        self.__header: View = Header()
        self.__footer: View = Footer()

    def add_view(self, view: View) -> ViewBuilder:
        self.__views.append(view)

    def add_header(self, header: Header) -> ViewBuilder:
        self.__header = header

    def add_footer(self, footer: Footer) -> ViewBuilder:
        self.__footer = footer

    def render(self) -> None:
        self.__clear_console()
        print(self.__generate())
        self.__reset()

    def __clear_console(self) -> None:
        if name == "posix":
            system("clear")
        else:
            system("cls")

    def __generate(self) -> str:
        views_generation: List[str] = []
        if len(self.__views) == 0:
            raise Exception()
        views_generation.append(self.__header.generate())
        for view in self.__views:
            views_generation.append(view.generate())
        views_generation.append(self.__footer.generate())
        return "".join(views_generation)

    def __reset(self) -> None:
        self.__views.clear()
