from chess.model.entities.round import Round
from chess.model.entity_managers.round_manager import RoundManager
from typing import List

from tinydb.table import Document
from chess.model.entities.match import Match
from chess.model.database.context import Context
from chess.model.entity_managers.entity_manager import EntityManager


class MatchManager(EntityManager):
    def __init__(self, context: Context):
        super(MatchManager, self).__init__(context)
        self.__round_manager: RoundManager = RoundManager(context)

    def get(self, id: int) -> Match:
        doc = self._context.matchs.get(doc_id=id)
        match: Match = Match.deserialize(doc)
        return match

    def get_all(self) -> List[Match]:
        documents: List[Document] = self._context.matchs.all()
        matchs: List[Match] = [Match.deserialize(doc) for doc in documents]
        return matchs

    def get_all_from_round(self, round_id: int) -> List[Match]:
        round: Round = self.__round_manager.get(round_id)
        matchs: List[Match] = [self.get(match_id) for match_id in round.matchs]
        return matchs

    def get_all_from_tournament(self, tournament_id: int) -> List[Match]:
        rounds: List[Round] = self.__round_manager.get_all_from_tournament(tournament_id)
        matchs: List[Match] = []
        for round in rounds:
            intermediate_matchs: List[Match] = self.get_all_from_round(round.id)
            for imatch in intermediate_matchs:
                matchs.append(imatch)
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
