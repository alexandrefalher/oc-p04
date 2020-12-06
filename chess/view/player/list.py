from chess.model.dto.dtos.player_dto import PlayerDto
from kview.request.request import Request
from chess.validation.could_be_number_validator import CouldBeNumberValidator
from chess.view.common.error_partial_view import ErrorPatialView
from chess.view.common.action_partial_view import ActionPartialView
from chess.view.common.title_partial_view import TitlePartialView
from chess.view.common.header_partial_view import HeaderPartialView
from chess.view.common.instruction_partial_view import InstructionPartialView
from typing import Any, List as TypeList
from kview.view.view import View
from kview.data_model.data_model import DataModel
import time


class List(View):
    def __init__(self, model: DataModel):
        super(List, self).__init__(model)
        self.__actions: TypeList[str] = []

    def generate(self, model: DataModel) -> str:
        view: str = ""
        dtos: List[PlayerDto] = model.get("entities")
        if dtos is not None:
            for dto in dtos:
                bd_local = time.localtime(dto.birth_date)
                birth_date = "{0}/{1}/{2}".format(bd_local.tm_mday, bd_local.tm_mon, bd_local.tm_year)
                self.__actions.append("Voir le détail de: {0} {1} {2}".format(dto.firstname, dto.lastname, birth_date))
        self.__actions.append("Retour")
        view += HeaderPartialView.generate()
        view += TitlePartialView.generate("Liste des joueurs")
        view += ActionPartialView.generate(self.__actions)
        view += ErrorPatialView.generate(model)
        view += InstructionPartialView.generate("Entrez le numéro correspondant à l'action que vous souhaitez effectuer")
        return view

    def flow(self, user_input: Any, model: DataModel) -> Request:
        dtos: List[PlayerDto] = model.get("entities")
        if not CouldBeNumberValidator.check(user_input):
            return None
        if int(user_input) >= 1 and int(user_input) <= len(self.__actions) - 1:
            dto_id: int = dtos[int(user_input) - 1].id
            return Request("/player/get", self.__module__, dto_id)
        elif user_input == str(len(self.__actions)):
            return Request("/player/menu", self.__module__, None)
        else:
            return None
