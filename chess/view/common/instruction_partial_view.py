class InstructionPartialView:
    @staticmethod
    def generate(message: str) -> str:
        view: str = "{0}:\n".format(message)
        return view
