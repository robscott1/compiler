class Declaration:

    def __init__(self, line, type, id):
        self.line = line
        self.type = type
        self.id = id

    def __repr__(self):
        return f"{self.id} ({self.type}) on line {self.line}"