from chess.model.entities.gender import Gender
from chess.model.entity_managers.gender_manager import GenderManager
import time
from chess.model.entities.player import Player
from chess.model.entity_managers.player_manager import PlayerManager
from chess.model.database.context import Context
from kview.client.client import Client
from kview.server.server import Server
from kview.router.route import Route
from kview.router.router import Router
from kview.config.config import Config


config: Config = Config("chess/config.yaml")
context: Context = Context(config)

# SEEDER FOR EXAMPLE
context.reset()
gender_manager: GenderManager = GenderManager(context)
player_manager: PlayerManager = PlayerManager(context)
gender_manager.create(Gender(0, "Homme"))
gender_manager.create(Gender(0, "Femme"))
player_manager.create(Player(0, "Pendragon", "Arthur", time.mktime(time.localtime()), 1, 10))

# -----------------

router: Router = Router([
    Route(endpoint="/", module="chess.controller.main_controller", controller="MainController", method="menu"),
    Route(endpoint="/tournament/menu", module="chess.controller.tournament_controller", controller="TournamentController", method="menu"),
    Route(endpoint="/player/menu", module="chess.controller.player_controller", controller="PlayerController", method="menu"),
    Route(endpoint="/player/get_all", module="chess.controller.player_controller", controller="PlayerController", method="get_all"),
    Route(endpoint="/player/get", module="chess.controller.player_controller", controller="PlayerController", method="get"),
    Route(endpoint="/player/to_update", module="chess.controller.player_controller", controller="PlayerController", method="to_update"),
    Route(endpoint="/player/update", module="chess.controller.player_controller", controller="PlayerController", method="update"),
    Route(endpoint="/player/to_create", module="chess.controller.player_controller", controller="PlayerController", method="to_create"),
    Route(endpoint="/player/create", module="chess.controller.player_controller", controller="PlayerController", method="create")
])
server: Server = Server(router, context)
client: Client = Client(server)


client.start()
