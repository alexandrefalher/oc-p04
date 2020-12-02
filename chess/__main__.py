from lib.client.client import Client
from lib.server.server import Server
from lib.router.route import Route
from lib.router.router import Router
from lib.config.config import Config


config: Config = Config("tournament/config.yaml")
router: Router = Router([
    Route(endpoint="/main/get", module="tournament.controller.main_controller", controller="MainController", method="get")
])
server: Server = Server(router)
client: Client = Client(config, server)


client.start()
