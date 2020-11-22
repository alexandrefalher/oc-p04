class Choice:
    def __init__(self, id: str, description: str, callback: lambda _: None):
        self.id: str = id
        self.description: str = description
        self.callback: lambda _: None = callback
