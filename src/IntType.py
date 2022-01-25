from src.Type import Type

class IntType(Type):

    def __init__(self):
        super()

    def equals(self, other):
        return isinstance(other, self.__class__)
