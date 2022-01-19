from Declaration import Declaration
from BoolType import BoolType
from Type import Type
from IntType import IntType
from BoolType import BoolType

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
    