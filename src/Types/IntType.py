from Type import Type

class IntType(Type):

    def __init__(self):
        super()
        self._ptr_status = ""

    def of_type(self, tc):
        return IntType()

    def equals(self, other):
        return isinstance(other, self.__class__)

    def to_text(self):
        return f"i32{self._ptr_status}"

    def cast_up(self):
        self._ptr_status = "*"
        return self

    def to_llvm_type(self):
        return "i32"


