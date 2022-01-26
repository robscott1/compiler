from Type import Type

class IntType(Type):

    def __init__(self):
        super()

    def of_type(self, tc):
        return IntType()

    def equals(self, other):
        return isinstance(other, self.__class__)
