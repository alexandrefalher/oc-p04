from typing import Any


class IsOnlyOneCharValidator:
    @staticmethod
    def check(param: Any) -> bool:
        param_length: int = len(param)
        return param_length == 1
