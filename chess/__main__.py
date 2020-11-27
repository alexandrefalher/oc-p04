from chess.controllers.mainController import MainController
from .config import Config


conf: Config = Config()
main: MainController = MainController(conf)
main.main_page()
