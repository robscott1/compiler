from Type import Type
from src.Declaration import Declaration
from src.IntType import IntType
from src.BoolType import BoolType

def type_switch(type, type_map):
    if type not in type_map:
        raise Exception("Error: Undeclared type.")
    return type_map.get(type)()

class DeclarationFactory:

    def generate(d_line, d_id, string_type, type_map):
        object_type = type_switch(string_type, type_map)
        return Declaration(d_line, object_type, d_id)
    