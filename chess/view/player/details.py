from chess.view.utils.utils import Utils
from chess.model.dto.dtos.player_dto import PlayerDto
from chess.model.dto.dtos.gender_dto import GenderDto
from kview.request.request import Request
from chess.validation.could_be_number_validator import CouldBeNumberValidator
from chess.validation.is_only_one_char_validator import IsOnlyOneCharValidator
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, List
from kview.view.view import View
from kview.data_model.data_model import DataModel


class Details(View):
    def __init__(self, model: DataModel):
        super(Details, self).__init__(model)

    def generate(self, model: DataModel) -> str:
        player_dto: PlayerDto = model.get("entity")
        gender_dtos: List[GenderDto] = model.get("genders")
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Détails du joueurs")
        view += "{0}: {1}\n".format("Prénom", player_dto.firstname)
        view += "{0}: {1}\n".format("Nom", player_dto.lastname)
        view += "{0}: {1}\n".format("Date de naissence", Utils.date_time_to_str(player_dto.birth_date))
        view += "{0}: {1}\n".format("Sexe", Utils.find_gender_name(player_dto, gender_dtos))
        view += "{0}: {1}\n".format("Classement", player_dto.ranking)
        view += "\n"
        view += ActionPartialView.generate(["Modifier", "Retour"])
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        dto: PlayerDto = model.get("entity")
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            return Request("/player/to_update", self.__module__, dto.id)
        elif user_input == "2":
            return Request("/player/get_all", self.__module__, None)
        else:
            return None
