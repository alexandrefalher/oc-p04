from ..router.route import Route
from typing import List


class Router:
    def __init__(self, routes: List[Route]):
        self.__routes: List[Route] = routes
        self.add_routes(routes)

    def add_routes(self, routes: List[Route]) -> None:
        for route in routes:
            self.add_route(route)

    def add_route(self, route: Route) -> None:
        route_id: int = self.is_route_exists(route.target)
        if route_id is not None:
            self.__routes[route_id] = route
        else:
            self.__routes.append(route)

    def get_route(self, target: str) -> Route:
        route_id: int = self.is_route_exists(target)
        return self.__routes[route_id]

    def is_route_exists(self, target: str) -> int:
        for i, route in enumerate(self.__routes):
            if route.target == target:
                return i
        return None
