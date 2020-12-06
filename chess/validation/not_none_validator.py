from typing import Any


class NotNoneValidator:
    @staticmethod
    def check(param: Any) -> bool:
        return param is not None
