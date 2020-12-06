from chess.model.database.context import Context


class Controller:
    def __init__(self, context: Context):
        self._context: Context = context
