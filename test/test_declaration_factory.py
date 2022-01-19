from src.DeclarationFactory import DeclarationFactory as df
from src.DeclarationFactory import type_switch
from src.IntType import IntType

def test_type_switch():
    assert type_switch("int").__class__ == IntType
