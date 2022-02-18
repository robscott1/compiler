import json
import subprocess
import sys

import pytest

from TypeChecker import TypeChecker


@pytest.fixture()
def type_checker():
    param = {
        "types": [{"line": 1, "id": "A", "fields": [
            {"line": 3, "type": "int", "id": "i"},
        ]}],
        "declarations": [{"line": 1, "type": "A", "id": "a"}],
        "functions": [{'line': 17, 'id': 'main',
                       'parameters': [{"line": 3, "type": "int", "id": "j"}],
                       'return_type': 'A',
                       'declarations': [{"line": 55, "type": "int", "id": "i"},
                                        {"line": 55, "type": "A", "id": "x"}],
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


@pytest.fixture()
def control_flow_example():
    param = {
        "types": [],
        "declarations": [],
        "functions": [
            {
                "line": 1,
                "id": "foo",
                "parameters": [
                    {
                        "line": 1,
                        "type": "int",
                        "id": "i"
                    }
                ],
                "return_type": "int",
                "declarations": [],
                "body": [
                    {
                        "line": 3,
                        "stmt": "return",
                        "exp": {
                            "line": 3,
                            "exp": "id",
                            "id": "i"
                        }
                    }
                ]
            },
            {
                "line": 6,
                "id": "bar",
                "parameters": [
                    {
                        "line": 6,
                        "type": "int",
                        "id": "i"
                    }
                ],
                "return_type": "int",
                "declarations": [],
                "body": [
                    {
                        "line": 8,
                        "stmt": "if",
                        "guard": {
                            "line": 8,
                            "exp": "binary",
                            "operator": ">",
                            "lft": {
                                "line": 8,
                                "exp": "id",
                                "id": "i"
                            },
                            "rht": {
                                "line": 8,
                                "exp": "num",
                                "value": "0"
                            }
                        },
                        "then": {
                            "stmt": "block",
                            "list": [
                                {
                                    "line": 10,
                                    "stmt": "return",
                                    "exp": {
                                        "line": 10,
                                        "exp": "num",
                                        "value": "1"
                                    }
                                }
                            ]
                        },
                        "else": {
                            "stmt": "block",
                            "list": [
                                {
                                    "line": 14,
                                    "stmt": "if",
                                    "guard": {
                                        "line": 14,
                                        "exp": "binary",
                                        "operator": "<",
                                        "lft": {
                                            "line": 14,
                                            "exp": "id",
                                            "id": "i"
                                        },
                                        "rht": {
                                            "line": 14,
                                            "exp": "num",
                                            "value": "0"
                                        }
                                    },
                                    "then": {
                                        "stmt": "block",
                                        "list": [
                                            {
                                                "line": 16,
                                                "stmt": "return",
                                                "exp": {
                                                    "line": 16,
                                                    "exp": "num",
                                                    "value": "1"
                                                }
                                            }
                                        ]
                                    },
                                    "else": {
                                        "stmt": "block",
                                        "list": [
                                            {
                                                "line": 20,
                                                "stmt": "return",
                                                "exp": {
                                                    "line": 20,
                                                    "exp": "num",
                                                    "value": "0"
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    }
    return TypeChecker(param)


def program_to_json(filename):
    with open(f"../json/{filename}.json", 'w') as out_file:
        subprocess.run(["java", "-jar", "../MiniCompiler.jar", filename], stdout=out_file)
    with open(f"../json/{filename}.json", 'r') as out_file:
        json_repr = dict(json.load(out_file))

    return json_repr
