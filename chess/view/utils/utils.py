from chess.model.entities.gender import Gender
from chess.model.entities.player import Player
import datetime
import time
from typing import Callable, Iterable, List, TypeVar

T = TypeVar('T')


class Utils:
    @staticmethod
    def find_gender_name(player_dto: Player, genders: List[Gender]) -> str:
        if player_dto.gender == 0:
            return ""
        player_dto_gender_name: str = ""
        for gender in genders:
            if gender.id == player_dto.gender:
                player_dto_gender_name = gender.name
        return player_dto_gender_name

    @staticmethod
    def find(iterable: Iterable[T], predicate: Callable[[T], bool]) -> T:
        for elt in iterable:
            if predicate(elt):
                return elt
        return None

    @staticmethod
    def date_time_to_str(date: time) -> str:
        if date == "":
            return ""
        bd_local = time.localtime(date)
        date_str = "{0}/{1}/{2}".format(bd_local.tm_mday, bd_local.tm_mon, bd_local.tm_year)
        return date_str

    @staticmethod
    def date_str_to_time(date: str) -> time:
        date_split: List[str] = date.split("/")
        date_datetime: datetime = datetime.date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
        date_timestamp = time.mktime(date_datetime.timetuple())
        return date_timestamp
