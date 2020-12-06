from chess.model.dto.dtos.player_dto import PlayerDto
from chess.model.entities.player import Player
from chess.model.entity_managers.gender_manager import GenderManager


class PlayerMapper:
    def __init__(self, gender_manager: GenderManager):
        self.__gender_manager: GenderManager = gender_manager

    def to_dto(self, player: Player) -> PlayerDto:
        return PlayerDto(
            id=player.id,
            lastname=player.lastname,
            firstname=player.firstname,
            birth_date=player.birth_date_timestamp,
            gender_id=player.gender_id,
            ranking=player.ranking
        )

    def to_entity(self, dto: PlayerDto) -> Player:
        return Player(
            id=dto.id,
            lastname=dto.lastname,
            firstname=dto.firstname,
            birth_date_timestamp=dto.birth_date,
            gender_id=dto.gender_id,
            ranking=dto.ranking
        )
