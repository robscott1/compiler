from src.TypeChecker import TypeChecker
from src.TypeDeclaration import TypeDeclaration
import pytest


@pytest.mark.parametrize(
    "in_dict, expected", [
        ({"line": 4, "id": "B", "fields": []}, False),
        ({"line": 5, "id": "H", "fields": []}, True),
        ({"line": 7, "id": "1L", "fields": []}, False)]
)
def test_check_type_decl(expected, in_dict):
    type_checker = TypeChecker()
    type0 = TypeDeclaration("3", "B", [])
    type_checker.type_map[type0.id] = type0
    in_type = TypeDeclaration(**in_dict)
    assert type_checker.check_type_decl(in_type) == expected

# Remember expected size is +2 for primitives
@pytest.mark.parametrize(
    "exp_size, input", [
        (3, {"types": [{"line": 1, "id": "A", "fields": [{"line": 3, "type": "int", "id": "i"}]}]}),
        (4, {"types": [{"line": 1, "id": "j", "fields": [{"line": 3, "type": "int", "id": "i"},
                                               {"line": 3, "type": "A", "id": "i"}]},
             {"line": 1, "id": "l", "fields": [{"line": 3, "type": "int", "id": "i"}]}]}
         )
    ]
)
def test_build_type_map(input, exp_size):
    type_checker = TypeChecker()
    type_map: dict = type_checker.build_type_map(input)
    assert len(type_map.keys()) == exp_size

def test_build_global_map():
    type_checker = TypeChecker()
    global_map: dict = type_checker.build_global_map()
