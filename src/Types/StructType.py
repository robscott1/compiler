from Type import Type


class StructType(Type):

    def __init__(self, id):
        self.id = id
        self._ptr_status = "*"

    def equals(self, other):
        return isinstance(other, self.__class__) and other.id == self.id

    def of_type(self, tc):
        return self

    def to_text(self, _to_ptr=None):
        res = f"%struct.{self.id}{self._ptr_status}"
        return res

    def to_llvm_type(self):
        return f"%struct.{self.id}"

    def cast_up(self):
        new = StructType(self.id)
        new._ptr_status = "**"
        return new

