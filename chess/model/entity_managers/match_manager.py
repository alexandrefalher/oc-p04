from typing import List

from tinydb.table import Document
from chess.model.entities.match import Match
from chess.model.database.context import Context
from chess.model.entity_managers.entity_manager import EntityManager


class MatchManager(EntityManager):
    def __init__(self, context: Context):
        super(MatchManager, self).__init__(context)

    def get(self, id: int) -> Match:
        doc = self._context.matchs.get(doc_id=id)
        match: Match = Match.deserialize(doc)
        return match

    def get_all(self) -> List[Match]:
        documents: List[Document] = self._context.matchs.all()
        matchs: List[Match] = [Match.deserialize(doc) for doc in documents]
        return matchs

    def create(self, match: Match) -> int:
        id: int = self._context.matchs.insert(Match.serialize(match))
        match.id = id
        self.update(id, match)
        return id

    def update(self, id: int, match: Match) -> int:
        ids: List[int] = self._context.matchs.update(Match.serialize(match), doc_ids=[id])
        return ids

    def delete(self, id: int) -> List[int]:
        raise NotImplementedError()
