from Type import Type

class BoolType(Type):
    def __init__(self):
        super();
        self._ptr_status = ""

    def of_type(self, tc):
        return BoolType()

    def equals(self, other):
        return isinstance(other, self.__class__)

    def to_text(self):
        return "i1"

    def cast_up(self):
        self._ptr_status = "*"
        return self

    def to_llvm_type(self):
        return "i1"

