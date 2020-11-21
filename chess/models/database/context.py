from tinydb.table import Table
from chess.config import Config
from tinydb import TinyDB
from tinydb.storages import MemoryStorage


class Context:
    def __init__(self, config: Config, in_memory_mode=False):
        self.__db_path = config.get_config("db_path")
        self.__init_db(self.__db_path, in_memory_mode)
        self.__init_tables()

    def __init_db(self, db_path: str, in_memory_mode: bool):
        if not in_memory_mode:
            self.__db = TinyDB(self.__db_path)
        else:
            self.__db = TinyDB(storage=MemoryStorage)

    def __init_tables(self):
        self.player: Table = self.__db.table("players")
        self.genders: Table = self.__db.table("genders")
        self.matchs: Table = self.__db.table("matchs")
        self.rounds: Table = self.__db.table("rounds")
        self.time_methods: Table = self.__db.table("time_methods")
        self.tournaments: Table = self.__db.table("tournaments")
