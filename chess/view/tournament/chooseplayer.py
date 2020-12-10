from chess.model.entities.tournament import Tournament
from kview.request.request import Request
from chess.validation.could_be_number_validator import CouldBeNumberValidator
from chess.validation.is_only_one_char_validator import IsOnlyOneCharValidator
from chess.validation.not_none_validator import NotNoneValidator
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, List
from kview.view.view import View
from kview.data_model.data_model import DataModel
from chess.view.utils.utils import Utils
from chess.model.entities.player import Player


class Chooseplayer(View):
    def __init__(self, model: DataModel):
        super(Chooseplayer, self).__init__(model)
        self.__tournament: Tournament = model.get("entity")
        self.__players: List[Player] = model.get("players")

    def generate(self, model: DataModel) -> str:
        actions: List[str] = []
        view: str = ""
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Création de tournois - assignation des joueurs")
        for i, player_id in enumerate(self.__tournament.players):
            if player_id != 0:
                player: Player = Utils.find(self.__players, lambda player: player.id == player_id)
                actions.append("Joueur {0} {1} {2} - {3}\n".format(player.firstname, player.lastname, player.birth_date, player.ranking))
            else:
                actions.append("Joueur Non assigné\n")
        view += "\n"
        actions.append("Retour")
        view += ActionPartialView.generate(actions)
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro de l'emplacement sur lequel vous voulez assigner un joueur")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if not NotNoneValidator.check(user_input):
            return None
        if not IsOnlyOneCharValidator.check(user_input):
            return None
        if not CouldBeNumberValidator.check(user_input):
            return None
        if 1 <= int(user_input) and int(user_input) <= 8:
            return Request("/tournament/searchplayer", self.__module__, {"tournament_id": self.__tournament.id, "tournament_player_index": int(user_input) - 1})
        elif user_input == "9":
            return Request("/tournament/update", self.__module__, self.__tournament)
        else:
            return None
