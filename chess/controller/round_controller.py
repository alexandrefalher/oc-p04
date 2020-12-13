from kview.data_model.data_model import DataModel
import time
from chess.model.entities.round import Round
from chess.model.entities.player import Player
from typing import Dict, List, Tuple
from chess.model.entities.tournament import Tournament
from chess.model.entities.match import Match
from chess.model.database.context import Context
from kview.controller.controller import Controller
from kview.response.response import Response
from chess.model.entity_managers.tournament_manager import TournamentManager
from chess.model.entity_managers.player_manager import PlayerManager
from chess.model.entity_managers.round_manager import RoundManager
from chess.model.entity_managers.match_manager import MatchManager
from chess.utils.utils import Utils


class RoundController(Controller):
    def __init__(self, context: Context):
        super(RoundController, self).__init__(context)
        self.__round_manager: RoundManager = RoundManager(context)
        self.__tournament_manager: TournamentManager = TournamentManager(context)
        self.__match_manager: MatchManager = MatchManager(context)
        self.__player_manager: PlayerManager = PlayerManager(context)

    def toupdate(self, args: Dict) -> Response:
        round_id: int = args["round_id"]
        tournament_id: int = args["tournament_id"]
        round: Round = self.__round_manager.get(round_id)
        matchs: List[Match] = self.__match_manager.get_all_from_round(round_id)
        players: List[Player] = self.__player_manager.get_all()
        model: DataModel = DataModel({"round": round, "matchs": matchs, "players": players, "tournament_id": tournament_id})
        return Response("Update", self.__module__, self.__class__.__name__, model)

    def update(self, args: Dict) -> Response:
        round: Round = args["round"]
        tournament_id: int = args["tournament_id"]
        self.__round_manager.update(round.id, round)
        matchs: List[Match] = self.__match_manager.get_all_from_round(round.id)
        players: List[Player] = self.__player_manager.get_all()
        model: DataModel = DataModel({"round": round, "matchs": matchs, "players": players, "tournament_id": tournament_id})
        return Response("Update", self.__module__, self.__class__.__name__, model)

    def updatematch(self, args: Dict) -> Response:
        round: Round = args["round"]
        match: Match = args["match"]
        tournament_id: int = args["tournament_id"]
        self.__match_manager.update(match.id, match)
        matchs: List[Match] = self.__match_manager.get_all_from_round(round.id)
        players: List[Player] = self.__player_manager.get_all()
        model: DataModel = DataModel({"round": round, "matchs": matchs, "players": players, "tournament_id": tournament_id})
        return Response("Update", self.__module__, self.__class__.__name__, model)

    def create(self, args: Dict) -> Response:
        tournament_id: int = args["tournament_id"]
        tournament_round_index: int = args["tournament_round_index"]
        tournament: Tournament = self.__tournament_manager.get(tournament_id)
        players: List[Player] = [self.__player_manager.get(player_id) for player_id in tournament.players]
        players_for_arrangement: List[Player] = players.copy()
        matchs: List[Match] = []
        if Utils.contains(tournament.rounds, lambda round_id: round_id != 0):
            matchs = self.next_arrangement(players_for_arrangement, tournament)
        else:
            matchs = self.first_arrangement(players_for_arrangement)
        for match in matchs:
            match.id = self.__match_manager.create(match)

        round_number: int = Utils.count(tournament.rounds, lambda round_id: round_id != 0)
        round: Round = Round(0, "Round{0}".format(round_number + 1), [match.id for match in matchs], time.mktime(time.localtime()), 0, False)
        round_id: int = self.__round_manager.create(round)
        tournament.rounds[tournament_round_index] = round_id
        self.__tournament_manager.update(tournament.id, tournament)
        model: DataModel = DataModel({"round": round, "matchs": matchs, "players": players, "tournament_id": tournament_id})
        return Response("Update", self.__module__, self.__class__.__name__, model)

    def first_arrangement(self, players: List[Player]) -> List[Match]:
        self.sort_by_rank(players)
        players_len_half: int = int(len(players) / 2)
        superior_half: List[Player] = players[:players_len_half]
        inferior_half: List[Player] = players[players_len_half:]
        matchs: List[Match] = []
        i: int = 0
        while i < players_len_half:
            match_result: Tuple[List, List] = ([superior_half[i].id, 0], [inferior_half[i].id, 0])
            matchs.append(Match(0, match_result))
            i += 1
        return matchs

    def next_arrangement(self, players: List[Player], tournament: Tournament) -> List[Match]:
        self.sort_by_points_and_rank(players, tournament)
        players_sorted: List[Player] = []
        while len(players) > 0:
            players_sorted.append(players[0])
            temp_player: Player = players.pop(0)
            if self.already_played_against(temp_player, players[0], tournament.rounds) and len(players) > 1:
                players_sorted.append(players[1])
                players.pop(1)
            else:
                players_sorted.append(players[0])
                players.pop(0)
        matchs: List[Match] = []
        i: int = 0
        while i < len(players_sorted):
            match_results: Tuple[List, List] = ([players_sorted[i].id, 0], [players_sorted[i + 1].id, 0])
            matchs.append(Match(0, match_results))
            i += 2
        return matchs

    def sort_by_rank(self, players: List[Player]) -> None:
        players.sort(key=lambda player: player.ranking)

    def already_played_against(self, player: Player, opponent: Player, round_ids: List[int]) -> bool:
        for round_id in round_ids:
            if round_id == 0:
                continue
            round: Round = self.__round_manager.get(round_id)
            for match_id in round.matchs:
                match: Match = self.__match_manager.get(match_id)
                if match.results[0][0] == player.id and match.results[1][0] == opponent.id or match.results[1][0] == player.id and match.results[0][0]:
                    return True
        return False

    def sort_by_points_and_rank(self, players: List[Player], tournament: Tournament) -> None:
        self.sort_by_points(players, tournament)
        i: int = 0
        changed: bool = False
        while True:
            if i == len(players) - 1:
                if changed:
                    i = 0
                    changed = False
                else:
                    break
            else:
                if players[i].ranking == players[i + 1].ranking:
                    current_player_points: int = self.player_points(players[i].id, tournament.rounds)
                    next_player_points: int = self.player_points(players[i + 1].id, tournament.rounds)
                    if current_player_points > next_player_points:
                        temp: Player = players[i + 1]
                        players[i + 1] = players[i]
                        players[i] = temp
                        changed = True
                i += 1

    def sort_by_points(self, players: List[Player], tournament: Tournament) -> None:
        players.sort(key=lambda player: self.player_points(player.id, tournament.rounds))

    def player_points(self, player_id: int, round_ids: List[int]) -> int:
        player_points: int = 0
        for round_id in round_ids:
            if round_id == 0:
                continue
            round: Round = self.__round_manager.get(round_id)
            for match_id in round.matchs:
                match: Match = self.__match_manager.get(match_id)
                player_points += self.find_player_points_in_match(match.results, player_id)
        return player_points

    def find_player_points_in_match(self, match_results: Tuple[List, List], player_id: int) -> int:
        if match_results[0][0] == player_id:
            return match_results[0][1]
        elif match_results[1][0] == player_id:
            return match_results[1][1]
        else:
            return 0
