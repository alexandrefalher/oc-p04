from typing import Any


class CouldBeNumberValidator:
    @staticmethod
    def check(param: Any) -> bool:
        try:
            int(param)
            return True
        except Exception:
            return False
