from typing import List

from chess.models.database.context import Context
from chess.models.entities.entity import Entity


class EntityManager:
    def __init__(self, context: Context):
        self._context: Context = context

    def get(self, id: int) -> Entity:
        raise NotImplementedError()

    def get_all(self) -> List[Entity]:
        raise NotImplementedError()

    def create(self, entity: Entity) -> int:
        raise NotImplementedError()

    def update(self, id: int, entity: Entity) -> int:
        raise NotImplementedError()

    def delete(self, id: int) -> int:
        raise NotImplementedError()
