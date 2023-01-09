
class ResourceNotFoundException(Exception):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

class TooPerfectException(Exception):
    def __init__(self, name: str):
        self.name = name