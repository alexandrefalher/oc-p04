from kview.client.client import Client
from kview.server.server import Server
from kview.router.route import Route
from kview.router.router import Router
from kview.config.config import Config


config: Config = Config("tournament/config.yaml")
router: Router = Router([
    Route(endpoint="/main/get", module="tournament.controller.main_controller", controller="MainController", method="get")
])
server: Server = Server(router)
client: Client = Client(config, server)


client.start()
