from Type import Type


class StructType(Type):

    def __init__(self, id):
        self.id = id

    def equals(self, other):
        return isinstance(other, self.__class__) and other.id == self.id

    def of_type(self, type_map):
        return self

    def to_value(self, _to_ptr=None):
        res = f"{self.id}" if _to_ptr is None else f"{self.id}*"
        return res
