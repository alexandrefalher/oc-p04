from typing import Dict, List
from tinydb.queries import where
from tinydb.table import Document

from chess.model.entities.tournament import Tournament
from chess.model.entity_managers.entity_manager import EntityManager
from chess.model.database.context import Context


class TournamentManager(EntityManager):
    def __init__(self, context: Context):
        super(TournamentManager, self).__init__(context)

    def is_unfinished_tournament(self) -> bool:
        tournament: Tournament = self.get_unfinished()
        return True if tournament is not None else False

    def get_unfinished(self) -> Tournament:
        doc: Document = self._context.tournaments.get(where("over").test(lambda p0: p0 is False))
        if doc is None:
            return None
        tournament: Tournament = Tournament.deserialize(doc)
        return tournament

    def get(self, id: int) -> Tournament:
        document = self._context.tournaments.get(doc_id=id)
        tournament: Tournament = Tournament.deserialize(document)
        return tournament

    def get_all(self) -> List[Tournament]:
        documents: List[Document] = self._context.tournaments.all()
        tournaments: List[Tournament] = [Tournament.deserialize(document) for document in documents]
        return tournaments

    def create(self, tournament: Tournament) -> int:
        tournament_serialized: Dict = Tournament.serialize(tournament)
        id: int = self._context.tournaments.insert(tournament_serialized)
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
