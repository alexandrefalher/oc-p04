from chess.views.view import View


class Footer(View):
    def __init__(self):
        super()

    def generate(self) -> str:
        lines: list[str] = [
            "--------------------------------------------------\n",
            "                       Footer                     \n",
            "--------------------------------------------------\n"
        ]
        return str.join(lines)
