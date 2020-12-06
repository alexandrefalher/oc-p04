from typing import List

from tinydb.table import Document
from chess.model.entity_managers.entity_manager import EntityManager
from chess.model.entities.round import Round
from chess.model.database.context import Context


class RoundManager(EntityManager):
    def __init__(self, context: Context):
        super(RoundManager, self).__init__(context)

    def get(self, id: int) -> Round:
        doc = self._context.rounds.get(doc_id=id)
        round: Round = Round.deserialize(doc)
        return round

    def get_all(self) -> List[Round]:
        documents: List[Document] = self._context.rounds.all()
        rounds: List[Round] = [Round.deserialize(doc) for doc in documents]
        return rounds

    def create(self, round: Round) -> int:
        id: int = self._context.rounds.insert(Round.serialize(round))
        round.id = id
        self.update(id, round)
        return id

    def update(self, id: int, round: Round) -> int:
        ids: List[int] = self._context.rounds.update(Round.serialize(round), id)
        return ids

    def delete(self, id: int) -> int:
        raise NotImplementedError()
