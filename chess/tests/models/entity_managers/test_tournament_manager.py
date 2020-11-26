from typing import List
from chess.models.entity_managers.tournament_manager import TournamentManager
from chess.config import Config
from chess.models.database.context import Context
from chess.models.entities.tournament import Tournament


class Test_TournamentManager:
    def setup_class(self):
        self.config: Config = Config("chess/tests/config.yaml")
        self.context: Context = Context(self.config, True)
        self.tournament_manager: TournamentManager = TournamentManager(self.context)

    def teardown_class(self):
        pass

    def setup_method(self):
        self.context.tournaments.insert({"id": 1, "name": "tournament1", "location": "Town1", "start_date_timestamp": "01/01/0001", "end_date_timestamp": "02/01/0001", "over": False, "round_count": 4, "rounds": "[]", "players": "[]", "time_method": 1, "description": "Description1"})

    def teardown_method(self):
        self.context.tournaments.truncate()

    def test_is_unfinished_tournamet(self) -> None:
        unfinished: int = self.tournament_manager.is_unfinished_tournament()
        assert unfinished

    def test_get(self) -> None:
        tournament: Tournament = self.tournament_manager.get(1)
        assert tournament.name == "tournament1"

    def test_get_all(self) -> None:
        tournaments: List[Tournament] = self.tournament_manager.get_all()
        assert len(tournaments) != 0

    def test_create(self) -> None:
        tournament: Tournament = Tournament(0, "tournament2", "Somewhere", "01/01/2020", "02/01/2020", True, 4, [1], [1], 1, "Description")
        id: int = self.tournament_manager.create(tournament)
        assert id != 0

    def test_update(self) -> None:
        tournament_old: Tournament = self.tournament_manager.get(1)
        tournament_location_old: str = tournament_old.location
        tournament_old.location = "Somewhere_somewhere"
        id: int = self.tournament_manager.update(1, tournament_old)
        tournament_updated: Tournament = self.tournament_manager.get(id)
        assert tournament_updated.location != tournament_location_old

    def test_delete(self) -> None:
        id: int = self.tournament_manager.delete(1)
        tournaments: List[Tournament] = self.tournament_manager.get_all()
        assert id == 1
        assert len(tournaments) == 0
