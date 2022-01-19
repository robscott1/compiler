from Type import Type
from src.Declaration import Declaration
from src.IntType import IntType
from src.BoolType import BoolType


def type_switch(t:str, type_map):
    if t == "int":
        return IntType()
    if t == "bool":
        return BoolType()
    if t in type_map:
        return type_map.get(t)
    return None


class DeclarationFactory:

    '''
    Temporarily axing the type switch. Java wants a Type, but a string
    will suffice and can access the TypeDeclaration when extra info is
    needed. Allows us to reference TypeDeclarations that have another
    instantiation of itself as a member. Otherwise the Type would be null.

    @:parameters:
        - d_line: (int) Declaration line number
        - d_id: (str) String id of declaration
        - string_type: (str) representation of itself
        - type_map: (dict) map of all types
    '''
    def generate(d_line: int, d_id: str, string_type: dict, type_map):
        # object_type = type_switch(string_type, type_map)
        return Declaration(d_line, string_type, d_id)
    