from src.Declaration import Declaration
from src.BoolType import BoolType
from src.Type import Type
from src.IntType import IntType
from src.BoolType import BoolType

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
    