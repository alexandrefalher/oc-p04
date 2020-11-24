class View:
    def __init__(self, model: dict):
        self._model: dict = model

    def generate(self) -> str:
        raise NotImplementedError()
