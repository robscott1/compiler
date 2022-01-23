from Type import Type
from src.Declaration import Declaration
from src.IntType import IntType
from src.BoolType import BoolType
from src.StructType import StructType


def type_switch(t:str):
    if t == "int":
        return IntType()
    if t == "bool":
        return BoolType()
    return StructType(t)


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
    def generate(line: int, id: str, type: dict):
        object_type = type_switch(type)
        return Declaration(line, object_type, id)
