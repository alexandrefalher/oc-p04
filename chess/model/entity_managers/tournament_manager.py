from typing import Dict, List

from tinydb.queries import where
from tinydb.table import Document
from chess.models.entities.tournament import Tournament
from chess.models.entity_managers.entity_manager import EntityManager
from chess.models.database.context import Context


class TournamentManager(EntityManager):
    def __init__(self, context: Context):
        super(TournamentManager, self).__init__(context)

    def is_unfinished_tournament(self) -> bool:
        unfinished: bool = self._context.tournaments.contains(where("over").test(lambda p0: p0 is False))
        return unfinished

    def get(self, id: int) -> Tournament:
        document: Document = self._context.tournaments.get(None, id)
        tournament: Tournament = Tournament.deserialize(document)
        return tournament

    def get_all(self) -> List[Tournament]:
        documents: List[Document] = self._context.tournaments.all()
        tournaments: List[Tournament] = [Tournament.deserialize(document) for document in documents]
        return tournaments

    def create(self, tournament: Tournament) -> int:
        serialized_tournament: Dict = tournament.serialize()
        id: int = self._context.tournaments.insert(serialized_tournament)
        tournament.id = id
        self.update(id, tournament)
        return id

    def update(self, id: int, tournament: Tournament) -> int:
        document: Document = Tournament.serialize(tournament)
        ids: List[int] = self._context.tournaments.update(document, doc_ids=[id])
        return ids[0]

    def delete(self, id: int) -> int:
        ids: List[int] = self._context.tournaments.remove(doc_ids=[id])
        return ids[0]
