import importlib
from kview.utils.console import Console
from typing import Any, List, Tuple

from ..data_model.data_model import DataModel
from ..response.response import Response
from ..client.processor import Processor
from ..request.request import Request
from ..server.server import Server
from ..view.view import View


class Client:
    def __init__(self, server: Server):
        self.__server: Server = server
        self.__request: Request = None
        self.__response: Response = None
        self.__view: View = None

    def process(self) -> None:
        for process in Processor([self._send_request, self._create_view, self._render_view]):
            if self.__request.endpoint == "/exit":
                Console.clear_console()
                break
            process()

    def start(self) -> None:
        self.__request = Request("/", "", DataModel(None))
        self.process()

    def _send_request(self) -> None:
        self.__response = self.__server.handle(self.__request)

    def _create_view(self) -> None:
        view_module: Any = self._import_view_module()
        view_class: Any = self._retrieve_view_class(view_module)
        self.__view = view_class(self.__response.model)

    def _render_view(self) -> None:
        self.__request = self.__view.execute()

    def _import_view_module(self) -> Any:
        view_module_name: str = self._retrieve_view_module(self.__response.source_module)
        view_module: Any = importlib.import_module(view_module_name)
        return view_module

    def _retrieve_view_class(self, view_module: Any) -> Any:
        view_class: Any = getattr(view_module, self.__response.target.capitalize())
        return view_class

    def _retrieve_view_module(self, module: str) -> str:
        module_base_path: Tuple[str, str] = self._extract_module_base_path(module)
        controller_subject: str = self._extract_controller_subject(module_base_path[1])
        view_module: str = module_base_path[0] + "." + "view" + "." + controller_subject + "." + self.__response.target.lower()
        return view_module

    def _extract_module_base_path(self, module: str) -> Tuple[str, str]:
        module_segments: List[str] = module.split(".")
        return (module_segments[0], module_segments[len(module_segments) - 1])

    def _extract_controller_subject(self, controller_module_name: str) -> str:
        subject: str = ""
        for char in controller_module_name:
            if char == "_":
                break
            subject += char
        return subject
