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
    def contains(iterable: Iterable[T], predicate: Callable[[T], bool]) -> bool:
        for elt in iterable:
            if predicate(elt):
                return True
        return False

    def count(iterable: Iterable[T], predicate: Callable[[T], bool]) -> int:
        count: int = 0
        for elt in iterable:
            if predicate(elt):
                count += 1
        return count

    @staticmethod
    def date_to_date_str(date: time) -> str:
        if date == "":
            return ""
        bd_local = time.localtime(date)
        date_str = "{0}/{1}/{2}".format(bd_local.tm_mday, bd_local.tm_mon, bd_local.tm_year)
        return date_str

    @staticmethod
    def date_to_datetime_str(datetime_: time) -> str:
        if datetime_ == "":
            return ""
        bd_local = time.localtime(datetime_)
        date_str = "{0}/{1}/{2} {3}:{4}:{5}".format(bd_local.tm_mday, bd_local.tm_mon, bd_local.tm_year, bd_local.tm_hour, bd_local.tm_min, bd_local.tm_sec)
        return date_str

    @staticmethod
    def date_str_to_date(date: str) -> time:
        date_split: List[str] = date.split("/")
        date_datetime: datetime = datetime.date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
        date_timestamp = time.mktime(date_datetime.timetuple())
        return date_timestamp

    @staticmethod
    def date_str_to_datetime(datetime_: str) -> time:
        datetime_split: List[str] = datetime_.split(" ")
        date_split: List[str] = datetime_split[0].split("/")
        time_split: List[str] = datetime_split[1].split(":")
        date_datetime: datetime = datetime.datetime(int(date_split[2]), int(date_split[1]), int(date_split[0]), int(time_split[2]), int(time_split[1]), int(time_split[0]))
        date_timestamp = time.mktime(date_datetime.timetuple())
        return date_timestamp
