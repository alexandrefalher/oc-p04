from ..data_model.data_model import DataModel


class Request:
    def __init__(self, endpoint: str, source: str, model: DataModel):
        self.endpoint: str = endpoint
        self.source: str = source
        self.model: DataModel = model
