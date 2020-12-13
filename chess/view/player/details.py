from chess.model.entities.gender import Gender
from chess.model.entities.player import Player
from chess.utils.utils import Utils
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
        player: Player = model.get("entity")
        genders: List[Gender] = model.get("genders")
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Détails du joueurs")
        view += "{0}: {1}\n".format("Prénom", player.firstname)
        view += "{0}: {1}\n".format("Nom", player.lastname)
        view += "{0}: {1}\n".format("Date de naissence", Utils.date_to_date_str(player.birth_date))
        view += "{0}: {1}\n".format("Sexe", Utils.find_gender_name(player, genders))
        view += "{0}: {1}\n".format("Classement", player.ranking)
        view += "\n"
        view += ActionPartialView.generate(["Modifier", "Retour"])
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        player: Player = model.get("entity")
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            return Request("/player/to_update", self.__module__, player.id)
        elif user_input == "2":
            return Request("/player/get_all", self.__module__, None)
        else:
            return None
