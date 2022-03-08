from Types.BoolType import BoolType
from Types.IntType import IntType
from Types.StructType import StructType


class Declaration:

    def __init__(self, line, type, id):
        self.line = line
        self.type = type
        self.id = id
        self.initialized = False

    def of_type(self, tc=None):
        if self.type == "int":
            return IntType()
        elif self.type == "bool":
            return BoolType()
        else:
            return StructType(self.id);

    def to_llvm_type(self):
        if self.type == "int" or isinstance(self.type, IntType):
            return "i32"
        elif self.type == "bool" or isinstance(self.type, BoolType):
            return "i1"
        else:
            return f"%struct.{self.type}"

    def to_global_declaration(self):
        return f"@{self.id} = common dso_local global {self.to_llvm_type()} 0"

