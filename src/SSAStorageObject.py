
class SSAStorageObject:

    def __init__(self, location, block):
        self.location = location
        self.block = block

    def to_text(self):
        return f"[{self.location}, {self.block.id}]"

    def to_value(self):
        return self.location