from typing import Any, Callable, List, TypeVar

from tinydb.table import Document
from chess.model.database.context import Context
from chess.model.entity_managers.entity_manager import EntityManager
from chess.model.entities.player import Player

T = TypeVar('T')


class PlayerManager(EntityManager):
    def __init__(self, context: Context):
        super(PlayerManager, self).__init__(context)

    def get(self, id: int) -> Player:
        doc = self._context.players.get(doc_id=id)
        player: Player = Player.deserialize(doc)
        return player

    def get_all(self) -> List[Player]:
        documents: List[Player] = self._context.players.all()
        players: List[Document] = [Player.deserialize(doc) for doc in documents]
        return players

    def get_sorted(self, sort_method: Callable[[Player], Any]) -> List[Player]:
        players: List[Player] = self.get_all()
        players.sort(key=sort_method)
        return players

    def create(self, player: Player) -> int:
        id: int = self._context.players.insert(Player.serialize(player))
        player.id = id
        self.update(id, player)
        return id

    def update(self, id: int, player: Player) -> List[int]:
        ids: List[int] = self._context.players.update(Player.serialize(player), doc_ids=[id])
        return ids

    def delete(self, id: int) -> List[int]:
        raise NotImplementedError()
