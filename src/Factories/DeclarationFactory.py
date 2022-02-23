from Type import Type
from Declaration import Declaration
from IntType import IntType
from BoolType import BoolType
from StructType import StructType


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
        - line: (int) Declaration line number
        - id: (str) String id of declaration
        - type: (str) representation of itself
    '''
    def generate(line: int, id: str, type: str):
        object_type = type_switch(type, )
        return Declaration(line, object_type, id)
