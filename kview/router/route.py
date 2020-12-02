class Route:
    def __init__(self, endpoint: str, module: str, controller: str, method: str):
        self.target: str = endpoint
        self.module: str = module
        self.controller: str = controller
        self.method: str = method
