from chess.views.view import View


class List(View):
    def __init__(self):
        super()

    def generate(self) -> str:
        lines: list[str] = [
            "- element 1\n",
            "- element 2\n",
            "- element 3\n"
        ]
        return "".join(lines)
