import pytest

from Declaration import Declaration
from Factories.ExpressionFactory import ExpressionFactory
from IntType import IntType


@pytest.mark.parametrize(
    "input", [
        ({"line": 31, "exp": "id", "id": "n"})
    ]
)
def test_identifier_expression_of_type(input, type_checker):
    id_exp = ExpressionFactory.generate(input)
    type_checker.global_map[input.get("id")] = \
        Declaration(55, IntType(), input.get("id"))
    t = id_exp.of_type(type_checker)
    assert t.__class__ == IntType


