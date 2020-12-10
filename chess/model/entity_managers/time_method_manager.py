from typing import List
from tinydb.table import Document
from chess.model.entity_managers.entity_manager import EntityManager
from chess.model.entities.time_method import TimeMethod
from chess.model.database.context import Context


class TimeMethodManager(EntityManager):
    def __init__(self, context: Context):
        super(TimeMethodManager, self).__init__(context)

    def get(self, id: int) -> TimeMethod:
        doc: Document = self._context.time_methods.get(doc_id=id)
        time_method: TimeMethod = TimeMethod.deserialize(doc)
        return time_method

    def get_all(self) -> List[TimeMethod]:
        documents: List[Document] = self._context.time_methods.all()
        time_methods: List[TimeMethod] = [TimeMethod.deserialize(doc) for doc in documents]
        return time_methods

    def create(self, time_method: TimeMethod) -> int:
        id: int = self._context.time_methods.insert(TimeMethod.serialize(time_method))
        time_method.id = id
        self.update(id, time_method)
        return id

    def update(self, id: int, time_method: TimeMethod) -> int:
        ids: List[int] = self._context.time_methods.update(TimeMethod.serialize(time_method), doc_ids=[id])
        return ids

    def delete(self, id: int) -> int:
        raise NotImplementedError()
