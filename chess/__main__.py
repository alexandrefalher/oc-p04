from chess.model.entities.time_method import TimeMethod
from chess.model.entity_managers.time_method_manager import TimeMethodManager
from chess.model.entity_managers.tournament_manager import TournamentManager
from chess.model.entities.tournament import Tournament
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
#context.reset()
gender_manager: GenderManager = GenderManager(context)
player_manager: PlayerManager = PlayerManager(context)
time_method_manager: TimeMethodManager = TimeMethodManager(context)
tournament_manager: TournamentManager = TournamentManager(context)
if len(context.genders.all()) == 0:
    gender_manager.create(Gender(0, "Homme"))
    gender_manager.create(Gender(0, "Femme"))
    player_manager.create(Player(0, "Pendragon", "Arthur", time.mktime(time.localtime()), 1, 1))
    player_manager.create(Player(0, "Dulac", "Lancelot", time.mktime(time.localtime()), 1, 2))
    player_manager.create(Player(0, "Decarmélides", "Leodagan", time.mktime(time.localtime()), 1, 3))
    player_manager.create(Player(0, "Degalles", "Perceval", time.mktime(time.localtime()), 1, 4))
    player_manager.create(Player(0, "Devannes", "Caradoc", time.mktime(time.localtime()), 1, 5))
    player_manager.create(Player(0, "ChevalierAuLion", "Yvain", time.mktime(time.localtime()), 1, 6))
    player_manager.create(Player(0, "LePetitPedestre", "Gauvain", time.mktime(time.localtime()), 1, 7))
    player_manager.create(Player(0, "Lesombre", "Méléagant", time.mktime(time.localtime()), 1, 8))
    time_method_manager.create(TimeMethod(0, "Bullet"))
    time_method_manager.create(TimeMethod(0, "Blitz"))
    time_method_manager.create(TimeMethod(0, "Coup rapide"))
    #tournament_manager.create(Tournament(0, "Tournois 1", "Rennes", time.mktime(time.localtime()), time.mktime(time.localtime()), True, 4, [], [], 1, "Description vide"))

# -----------------

router: Router = Router([
    Route(endpoint="/", module="chess.controller.main_controller", controller="MainController", method="menu"),
    Route(endpoint="/tournament/menu", module="chess.controller.tournament_controller", controller="TournamentController", method="menu"),
    Route(endpoint="/tournament/details", module="chess.controller.tournament_controller", controller="TournamentController", method="get"),
    Route(endpoint="/tournament/list", module="chess.controller.tournament_controller", controller="TournamentController", method="get_all"),
    Route(endpoint="/tournament/update", module="chess.controller.tournament_controller", controller="TournamentController", method="update"),
    Route(endpoint="/tournament/continue", module="chess.controller.tournament_controller", controller="TournamentController", method="continue_tournament"),
    Route(endpoint="/tournament/new", module="chess.controller.tournament_controller", controller="TournamentController", method="create"),
    Route(endpoint="/tournament/chooseplayer", module="chess.controller.tournament_controller", controller="TournamentController", method="chooseplayer"),
    Route(endpoint="/tournament/searchplayer", module="chess.controller.tournament_controller", controller="TournamentController", method="searchplayer"),
    Route(endpoint="/tournament/choosetimemethod", module="chess.controller.tournament_controller", controller="TournamentController", method="choosetimemethod"),
    Route(endpoint="/tournament/chooseround", module="chess.controller.tournament_controller", controller="TournamentController", method="chooseround"),
    Route(endpoint="/round/update", module="chess.controller.round_controller", controller="RoundController", method="update"),
    Route(endpoint="/round/toupdate", module="chess.controller.round_controller", controller="RoundController", method="toupdate"),
    Route(endpoint="/round/create", module="chess.controller.round_controller", controller="RoundController", method="create"),
    Route(endpoint="/round/updatematch", module="chess.controller.round_controller", controller="RoundController", method="updatematch"),
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
