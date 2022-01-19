from src.TypeChecker import TypeChecker as tc
from src.TypeDeclaration import TypeDeclaration
import pytest

@pytest.mark.parametrize(
    "in_type", [TypeDeclaration("4", "H", [])]
)
def test_check_type_decl(in_type):
    type_checker = tc()
    type0 = TypeDeclaration("3", "B", [])
    type_checker.types[type0.id] = type0
    assert tc.check_type_decl(in_type)
