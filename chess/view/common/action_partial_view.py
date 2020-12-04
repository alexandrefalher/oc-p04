from typing import List


class ActionPartialView:
    @staticmethod
    def generate(choices: List[str]) -> str:
        view: str = ""
        for i, choice in enumerate(choices):
            view += "{0} - {1} \n".format(i, choice)
        view += "\n"
        return view
