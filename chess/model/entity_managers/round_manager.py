from chess.model.entities.tournament import Tournament
from chess.model.entity_managers.tournament_manager import TournamentManager
from typing import List

from tinydb.table import Document
from chess.model.entity_managers.entity_manager import EntityManager
from chess.model.entities.round import Round
from chess.model.database.context import Context


class RoundManager(EntityManager):
    def __init__(self, context: Context):
        super(RoundManager, self).__init__(context)
        self.__tournament_manager: TournamentManager = TournamentManager(context)

    def get(self, id: int) -> Round:
        doc = self._context.rounds.get(doc_id=id)
        round: Round = Round.deserialize(doc)
        return round

    def get_all(self) -> List[Round]:
        documents: List[Document] = self._context.rounds.all()
        rounds: List[Round] = [Round.deserialize(doc) for doc in documents]
        return rounds

    def get_all_from_tournament(self, tournament_id: int) -> List[Round]:
        tournament: Tournament = self.__tournament_manager.get(tournament_id)
        rounds: List[Round] = []
        for round_id in tournament.rounds:
            rounds.append(self.get(round_id))
        return rounds

    def create(self, round: Round) -> int:
        id: int = self._context.rounds.insert(Round.serialize(round))
        round.id = id
        self.update(id, round)
        return id

    def update(self, id: int, round: Round) -> int:
        ids: List[int] = self._context.rounds.update(Round.serialize(round), doc_ids=[id])
        return ids

    def delete(self, id: int) -> int:
        raise NotImplementedError()
