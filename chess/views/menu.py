from chess.views.list import List
from typing import Dict
from chess.views.view import View


class Menu(View):
    def __init__(self, choices: Dict[int, List]):
        super()
        self.__choices: Dict[int, List] = choices

    def generate(self) -> str:
        result: str = ""
        return result.join([self.__generate_line(choice) for choice in self.__choices])

    def __generate_line(self, choice: int) -> str:
        return str(choice) + " - " + self.__choices[choice][0] + "\n"
