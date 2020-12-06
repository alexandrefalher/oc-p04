from inspect import FullArgSpec
from chess.model.database.context import Context
import importlib
from typing import Any
import inspect

from ..data_model.data_model import DataModel
from ..router.route import Route
from ..router.router import Router
from ..request.request import Request
from ..response.response import Response
from ..controller.controller import Controller


class Server:
    def __init__(self, router: Router, context: Context):
        self.__router: Router = router
        self.__context: Context = context

    def handle(self, request: Request) -> Response:
        route: Route = self._find_route(request.endpoint)
        controller: Controller = self._create_controller(route)
        response: Response = self._call_method(controller, route.method, request.data)
        return response

    def _find_route(self, endpoint: str) -> Route:
        route: Route = self.__router.get_route(endpoint)
        return route

    def _create_controller(self, route: Route) -> Controller:
        controller_module: Any = importlib.import_module(route.module)
        controller_class: Any = getattr(controller_module, route.controller)
        controller: Controller = controller_class(self.__context)
        return controller

    def _call_method(self, controller: Controller, method: str, data: Any) -> Response:
        method: Any = getattr(controller, method)
        spec: FullArgSpec = inspect.getfullargspec(method)
        if len(spec.args) > 1:
            response: Response = method(data)
        else:
            response: Response = method()
        return response
