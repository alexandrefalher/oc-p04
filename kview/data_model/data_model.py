from typing import Any, Dict


class DataModel:
    def __init__(self, data: Dict[str, Any]):
        self.data: Dict[str, Any] = data if data is not None else {}

    def get(self, key: str) -> Any:
        return self.data.get(key)

    def add(self, key: str, value: Any) -> bool:
        if not self._is_key_exists(key):
            self.data[key] = value
            return True
        return False

    def update(self, key: str, value: Any) -> bool:
        if not self._is_key_exists(key):
            return False
        else:
            self.data[key] = value
            return True

    def remove(self, key: str) -> bool:
        if not self._is_key_exists(key):
            return False
        else:
            self.data.pop(key)
            return True

    def _is_key_exists(self, key: str) -> bool:
        result = self.data.get(key)
        return result is not None
