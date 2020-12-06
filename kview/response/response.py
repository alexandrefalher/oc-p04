from kview.data_model.data_model import DataModel


class Response:
    def __init__(self, target: str, source_module: str, source_controller: str, model: DataModel):
        self.target: str = target
        self.source_module: str = source_module
        self.source_controller: str = source_controller
        self.model: DataModel = model
