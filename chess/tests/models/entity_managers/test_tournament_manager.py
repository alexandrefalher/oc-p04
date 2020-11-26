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
        pass

    def teardown_method(self):
        pass

    def test_create(self) -> None:
        tournament: Tournament = Tournament(1, "tournament1", "Somewhere", "01/01/2020", "02/01/2020", 4, [1], [1], 1, "Description")
        id: int = self.tournament_manager.create(tournament)
        assert id != 0
