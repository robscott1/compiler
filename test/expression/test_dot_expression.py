import pytest

from Expressions.DotExpression import DotExpression
from Factories.ExpressionFactory import ExpressionFactory
from IntType import IntType


@pytest.mark.parametrize(
    "input", [
        {"line": 4, "left": {"line": 5, "exp": "id", "id": "a"}, "id": "i"}
    ]
)
def test_dot_expression_of_type(input, type_checker):
    input["left"] = ExpressionFactory.generate(input.get("left"))
    dot = DotExpression(**input)
    t = dot.of_type(type_checker)
    assert t.__class__ == IntType
