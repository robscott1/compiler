from Type import Type


class NullType(Type):

    def __init__(self):
        pass

    def equals(self, other):
        return isinstance(other, self.__class__)

    def to_value(self):
        return "void"

    def of_type(self, tc=None):
        return "void"
