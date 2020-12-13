from chess.model.entities.gender import Gender
from chess.model.entities.player import Player
from kview.request.request import Request
from chess.validation.could_be_number_validator import CouldBeNumberValidator
from chess.validation.is_only_one_char_validator import IsOnlyOneCharValidator
from chess.validation.not_none_validator import NotNoneValidator
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, List, Union
from kview.view.view import View
from kview.data_model.data_model import DataModel
from chess.utils.utils import Utils


class Update(View):
    def __init__(self, model: DataModel):
        super(Update, self).__init__(model)

    def generate(self, model: DataModel) -> str:
        player: Player = model.get("entity")
        genders: List[Gender] = model.get("genders")
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Modifier le joueur")
        view += "{0}: {1}\n".format("Prénom", player.firstname)
        view += "{0}: {1}\n".format("Nom", player.lastname)
        view += "{0}: {1}\n".format("Date de naissance", Utils.date_to_date_str(player.birth_date))
        view += "{0}: {1}\n".format("Sexe", Utils.find_gender_name(player, genders))
        view += "{0}: {1}\n".format("Classement", player.ranking)
        view += "\n"
        view += ActionPartialView.generate(["Modifier prénom", "Modifier nom", "Modifier date de naissance", "Modifier sexe", "Modifier classement", "Enregistrer", "Retour"])
        view += ErrorPatialView.generate(model)
        instruction: str = model.get("instruction")
        if instruction is None:
            instruction = "Entrez le numéro correspondant à l'action que vous souhaitez effectuer"
        view += InstructionPartialView.generate(instruction)
        return view

    def flow(self, user_input: Any, model: DataModel) -> Union[str, None]:
        player: Player = model.get("entity")
        if not NotNoneValidator.check(user_input):
            return None
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if user_input == "1":
            player.firstname = input("Nouveau prénom >>> ")
            model.update("entity", player)
            return None
        elif user_input == "2":
            player.lastname = input("Nouveau nom >>> ")
            model.update("entity", player)
            return None
        elif user_input == "3":
            birth_date: str = input("Nouvelle date de naissance (format JJ/MM/AAAA) >>> ")
            player.birth_date = Utils.date_str_to_date(birth_date)
            return None
        elif user_input == "4":
            gender_id_str = input("Nouveau sexe (1 pour Homme, 2 pour Femme) >>> ")
            player.gender = int(gender_id_str)
            model.update("entity", player)
            return None
        elif user_input == "5":
            ranking_str = input("Nouveau classement >>> ")
            player.ranking = int(ranking_str)
            model.update("entity", player)
            return None
        elif user_input == "6":
            return Request("/player/update", self.__module__, player)
        elif user_input == "7":
            return Request("/player/get_all", self.__module__, None)
        else:
            return None
