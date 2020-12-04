from typing import Any


class IsNumberValidator:
    @staticmethod
    def check(param: Any) -> bool:
        param_type = type(param)
        return param_type is int
