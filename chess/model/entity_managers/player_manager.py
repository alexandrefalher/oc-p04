from typing import List

from chess.model.database.context import Context
from chess.model.entity_managers.entity_manager import EntityManager
from chess.model.entities.player import Player


class PlayerManager(EntityManager):
    def __init__(self, context: Context):
        super(PlayerManager, self).__init__(context)

    def get(self, id: int) -> Player:
        player: Player = self._context.players.get(id)
        return player

    def get_all(self) -> List[Player]:
        players: List[Player] = self._context.players.all()
        return players

    def create(self, player: Player) -> int:
        id: int = self._context.players.insert(player.serialize())
        player.id = id
        self.update(player, id)
        return id

    def update(self, id: int, player: Player) -> List[int]:
        ids: List[int] = self._context.players.update(player, id)
        return ids

    def delete(self, id: int) -> List[int]:
        raise NotImplementedError()
