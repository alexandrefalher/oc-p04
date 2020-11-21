from chess.views.view import View


class Menu(View):
    def __init__(self):
        super()

    def generate(self) -> str:
        lines: list[str] = [
            "What do you want to do ?",
            "1 - Choice 1",
            "2 - Choice 2",
            "3 - Choice 3"
        ]
        return str.join(lines)
