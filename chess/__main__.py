from chess.controllers.mainController import MainController
from .config import Config


conf: Config = Config()
main: MainController = MainController()
main.main_page()
