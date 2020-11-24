from chess.views.view import View


class Header(View):
    def __init__(self):
        super()

    def generate(self) -> str:
        lines: list[str] = [
            "**************************************************\n",
            "**                    Header                    **\n",
            "**************************************************\n"
        ]
        return "".join(lines)
