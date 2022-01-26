from Type import Type

class BoolType(Type):
    def __init__(self):
        super();

    def of_type(self, tc):
        return BoolType()

    def equals(self, other):
        return isinstance(other, self.__class__)
