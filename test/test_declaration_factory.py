from src.BoolType import BoolType
from src.DeclarationFactory import type_switch
from src.IntType import IntType


def test_type_switch():
    type_map = {
        "int": IntType,
        "bool": BoolType,
    }
    assert type_switch("int", type_map).__class__ == IntType
