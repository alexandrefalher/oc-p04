from typing import List

from tinydb.table import Document
from chess.model.database.context import Context
from chess.model.entity_managers.entity_manager import EntityManager
from chess.model.entities.gender import Gender


class GenderManager(EntityManager):
    def __init__(self, context: Context):
        super(GenderManager, self).__init__(context)

    def get(self, id: int) -> Gender:
        doc = self._context.genders.get(doc_id=id)
        gender: Gender = Gender.deserialize(doc)
        return gender

    def get_all(self) -> List[Gender]:
        docs: List[Document] = self._context.genders.all()
        genders: List[Gender] = [Gender.deserialize(doc) for doc in docs]
        return genders

    def create(self, gender: Gender) -> int:
        id: int = self._context.genders.insert(Gender.serialize(gender))
        gender.id = id
        self.update(id, gender)
        return id

    def update(self, id: int, gender: Gender) -> int:
        ids: List[int] = self._context.genders.update(Gender.serialize(gender), doc_ids=[id])
        return ids

    def delete(self, id: int) -> int:
        raise NotImplementedError()
