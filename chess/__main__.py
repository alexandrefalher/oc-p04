from kview.client.client import Client
from kview.server.server import Server
from kview.router.route import Route
from kview.router.router import Router
from kview.config.config import Config


config: Config = Config("chess/config.yaml")
router: Router = Router([
    Route(endpoint="/", module="chess.controller.main_controller", controller="MainController", method="menu"),
    Route(endpoint="/tournament/menu", module="chess.controller.tournament_controller", controller="TournamentController", method="menu"),
    Route(endpoint="/player/menu", module="chess.controller.player_controller", controller="PlayerController", method="menu")
])
server: Server = Server(router)
client: Client = Client(server)


client.start()
