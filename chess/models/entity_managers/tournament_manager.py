from typing import List
from chess.models.entities.tournament import Tournament
from chess.models.entity_managers.entity_manager import EntityManager
from chess.models.database.context import Context


class TournamentManager(EntityManager):
    def __init__(self, context: Context):
        super(TournamentManager, self).__init__(context)

    def get(self, id: int) -> Tournament:
        tournament: Tournament = self._context.tournaments.get(id)
        return tournament

    def get_all(self) -> List[Tournament]:
        tournements: List[Tournament] = self._context.tournaments.all()
        return tournements

    def create(self, tournament: Tournament) -> int:
        id: int = self._context.tournaments.insert(tournament.serialize())
        tournament.id = id
        self.update([id], tournament.serialize())
        return id

    def update(self, id: int, tournament: Tournament) -> List[int]:
        ids: List[int] = self._context.tournaments.update(tournament, doc_ids=id)
        return ids

    def delete(self, id: int) -> List[int]:
        ids: List[int] = self._context.tournaments.remove(doc_ids=id)
        return ids
