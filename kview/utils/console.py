from os import system, name


class Console:
    @staticmethod
    def clear_console() -> None:
        if name == "posix":
            system("clear")
        else:
            system("cls")
