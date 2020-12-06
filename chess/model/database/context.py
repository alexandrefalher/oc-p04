from tinydb.table import Table
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

from kview.config.config import Config


class Context:
    def __init__(self, config: Config, in_memory_mode=False):
        self.__db_path = config.get_config("db_path")
        self.__init_db(in_memory_mode)
        self.__init_tables()

    def __init_db(self, in_memory_mode: bool):
        if not in_memory_mode:
            self.__db = TinyDB(self.__db_path)
        else:
            self.__db = TinyDB(storage=MemoryStorage)

    def reset(self) -> None:
        if self.__db is not None:
            self.__db.drop_tables()

    def __init_tables(self):
        self.players: Table = self.__db.table("players")
        self.genders: Table = self.__db.table("genders")
        self.matchs: Table = self.__db.table("matchs")
        self.rounds: Table = self.__db.table("rounds")
        self.time_methods: Table = self.__db.table("time_methods")
        self.tournaments: Table = self.__db.table("tournaments")
