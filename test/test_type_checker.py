from src.TypeChecker import TypeChecker
from src.TypeDeclaration import TypeDeclaration
import pytest

@pytest.mark.parametrize(
    "in_dict, expected", [
        ({"line":4, "id":"B", "fields":[]}, False),
        ({"line":5, "id":"H", "fields":[]}, True),
        ({"line":7, "id":"1L", "fields":[]}, False)]
)
def test_check_type_decl(expected, in_dict):
    type_checker = TypeChecker()
    type0 = TypeDeclaration("3", "B", [])
    type_checker.types[type0.id] = type0
    in_type = TypeDeclaration(**in_dict)
    assert type_checker.check_type_decl(in_type) == expected
