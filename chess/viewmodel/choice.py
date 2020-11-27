class Choice:
    def __init__(self, id: str, description: str, callback: lambda param: None):
        self.id: str = id
        self.description: str = description
        self.callback: lambda param: None = callback
