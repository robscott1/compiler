from Types.BoolType import BoolType
from Types.IntType import IntType
from Types.StructType import StructType


class Declaration:

    def __init__(self, line, type, id):
        self.line = line
        self.type = type
        self.id = id
        self.initialized = False

    def of_type(self, tc):
        if self.type == "int":
            return IntType()
        elif self.type == "bool":
            return BoolType()
        else:
            return StructType(self.id);

