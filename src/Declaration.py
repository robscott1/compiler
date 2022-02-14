from Instructions.Instruction import Instruction


class Declaration:

    def __init__(self, line, type, id):
        self.line = line
        self.type = type
        self.id = id
        self.initialized = False

    def __repr__(self):
        return f"{self.id} ({self.type}) on line {self.line}"

