from TypeChecker import TypeChecker
from TypeDeclaration import TypeDeclaration
import pytest


# @pytest.mark.parametrize(
#     "in_dict, expected", [
#         ({"line": 4, "id": "B", "fields": []}, False),
#         ({"line": 5, "id": "H", "fields": []}, True),
#         ({"line": 7, "id": "1L", "fields": []}, False)]
# )
# def test_check_type_decl(expected, in_dict):
#     type_checker = TypeChecker()
#     type0 = TypeDeclaration("3", "B", [])
#     type_checker.type_map[type0.id] = type0
#     in_type = TypeDeclaration(**in_dict)
#     assert type_checker.check_type_decl(in_type) == expected

# Remember expected size is +2 for primitives
@pytest.mark.parametrize(
    "exp_size, input", [
        (3, [{"line": 1, "id": "A", "fields": [{"line": 3, "type": "int", "id": "i"}]}]),
        (4, [{"line": 1, "id": "j", "fields": [{"line": 3, "type": "int", "id": "i"},
                                               {"line": 3, "type": "A", "id": "i"}]},
             {"line": 1, "id": "l", "fields": [{"line": 3, "type": "int", "id": "i"}]}]
         )
    ]
)
def test_build_type_map(input, exp_size):
    type_map: dict = TypeChecker.build_type_map(input)
    assert len(type_map.keys()) == exp_size

@pytest.mark.parametrize(
    "types, declarations, exp_size", [
        ([{"line": 1, "id": "A", "fields": []}],
         [{"line": 1, "type": "A", "id": "a"}], 1),
        ({"line": 1, "id": "A", "fields": []},
         [{"line": 1, "type": "A", "id": "a"},
                           {"line": 3, "type": "int", "id": "b"}], 2)
    ]
)
def test_build_global_map(exp_size, declarations, types):
    global_map: dict = TypeChecker.build_global_map(declarations)
    assert len(global_map.keys()) == exp_size

@pytest.mark.parametrize(
    "input", [
        ({"types": [{"line": 1, "id": "A", "fields": []}],
          "declarations": [{"line": 1, "type": "A", "id": "a"}],
          "functions": [{'line': 17, 'id': 'f',
                        'parameters': [], 'return_type': 'A',
                        'declarations': [], "body": []}]
          })
    ]
)
def test_type_checker_init(input):
    tc = TypeChecker(input)
    assert hasattr(tc, "type_map")
    assert hasattr(tc, "global_map")
    assert hasattr(tc, "fn_map")

# @pytest.mark.parametrize(
#     "types, declarations", [
#         ({"line": 1, "id": "A", "fields": []},
#          {"declarations": [{"line": 1, "type": "B", "id": "a"}]}),
#         ({"line": 1, "id": "A", "fields": []},
#          {"declarations": [{"line": 1, "type": "A", "id": "a"},
#                            {"line": 3, "type": "int", "id": "2b"}]}),
#         ({"line": 1, "id": "A", "fields": []},
#          {"declarations": [{"line": 1, "type": "A", "id": "1a"},
#                            {"line": 3, "type": "int", "id": "2b"}]})
#     ]
# )
# def test_build_global_map_unhappy_path(declarations, types):
#     type_checker = TypeChecker()
#     type_checker.type_map["A"] = TypeDeclaration(**types)
#     with pytest.raises(Exception):
#         type_checker.build_global_map(declarations)


