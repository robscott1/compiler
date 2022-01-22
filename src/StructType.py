from Type import Type


class StructType(Type):

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"Struct {self.id}"