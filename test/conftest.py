import pytest

from TypeChecker import TypeChecker


@pytest.fixture()
def type_checker():
    param = {
        "types": [{"line": 1, "id": "A", "fields": [
            {"line": 3, "type": "int","id": "i"},
        ]}],
        "declarations": [{"line": 1, "type": "A", "id": "a"}],
        "functions": [{'line': 17, 'id': 'main',
                       'parameters': [{"line": 3, "type": "int", "id": "j"}],
                       'return_type': 'A',
                       'declarations': [{"line": 55, "type": "int", "id": "i"}],
                       "body": []},
                      {'line': 17, 'id': 'f',
                       'parameters': [{"line": 3, "type": "int", "id": "j"},
                                      {"line": 3, "type": "bool", "id": "c"}],
                       'return_type': 'int',
                       'declarations': [{"line": 55, "type": "int", "id": "i"}],
                       "body": []}
                      ]
    }
    return TypeChecker(param)
