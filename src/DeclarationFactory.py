from Declaration import Declaration
from natives.BoolType import BoolType
from natives.Type import Type
from natives.IntType import IntType
from natives.BoolType import BoolType

def type_switch(type):
    if type == "int":
        return IntType()
    elif type == "bool":
        return BoolType()
    return None

class DeclarationFactory:

    def generate(line, id, type):
        type = type_switch(type)
        return Declaration(line, type, id)
    