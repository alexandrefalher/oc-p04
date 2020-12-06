from chess.model.entities.gender import Gender
from chess.model.dto.dtos.gender_dto import GenderDto


class GenderMapper:
    def __init__(self):
        pass

    def to_dto(self, gender: Gender) -> GenderDto:
        return GenderDto(
            id=gender.id,
            name=gender.name
        )

    def to_entity(self, dto: GenderDto) -> Gender:
        return Gender(
            id=dto.id,
            name=dto.name
        )