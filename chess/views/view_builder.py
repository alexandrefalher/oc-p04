from __future__ import annotations
from chess.views.view import View


class ViewBuilder:
    def __init__(self):
        self.__views: list[View] = []

    def add_view(self, view: View) -> ViewBuilder:
        self.__views.append(view)

    def generate(self) -> str:
        if len(self.__views) == 0:
            raise Exception()
        return str.join(view.generate() for view in self.__views)
