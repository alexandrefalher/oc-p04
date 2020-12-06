from typing import Any


class Request:
    def __init__(self, endpoint: str, source: str, data: Any):
        self.endpoint: str = endpoint
        self.source: str = source
        self.data: Any = data
