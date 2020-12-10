from chess.model.entities.tournament import Tournament
from chess.view.utils.utils import Utils
from chess.model.entities.player import Player
from kview.request.request import Request
from chess.validation.could_be_number_validator import CouldBeNumberValidator
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, List
from kview.view.view import View
from kview.data_model.data_model import DataModel


class Searchplayer(View):
    def __init__(self, model: DataModel):
        super(Searchplayer, self).__init__(model)
        self.__actions: List[str] = []
        self.__tournament: Tournament = model.get("tournament")
        self.__players: List[Player] = model.get("players")
        self.__player_index: int = model.get("tournament_player_index")

    def generate(self, model: DataModel) -> str:
        view: str = ""
        if self.__players is not None:
            for player in self.__players:
                if Utils.find(self.__tournament.players, lambda player_id: player_id == player.id):
                    self.__players.remove(player)
                    continue
                birth_date = Utils.date_time_to_str(player.birth_date)
                self.__actions.append("Assigner: {0} {1} {2} - {3}".format(player.firstname, player.lastname, birth_date, player.ranking))
        model.update("entities", self.__players)
        self.__actions.append("Retour")
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Création de tournois - assignation des joueurs - liste")
        view += ActionPartialView.generate(self.__actions)
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        if not CouldBeNumberValidator.check(user_input):
            return None
        if 1 <= int(user_input) and int(user_input) < len(self.__actions):
            selected_player: Player = self.__players[int(user_input) - 1]
            self.__tournament.players[self.__player_index] = selected_player.id
            return Request("/tournament/update", self.__module__, self.__tournament)
        elif user_input == str(len(self.__actions)):
            return Request("/tournament/chooseplayer", self.__module__, self.__tournament.id)
        else:
            return None
