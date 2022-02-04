from Type import Type


class NullType(Type):

    def __init__(self):
        pass

    def equals(self, other):
        return isinstance(other, self.__class__)
