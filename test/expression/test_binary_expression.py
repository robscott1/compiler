import pytest

from Expressions.BinaryExpression import BinaryExpression
from Expressions.Expression import Expression
from Operator import Operator


@pytest.mark.parametrize(
    "operator, exp", [
        ("*", Operator.TIMES),
        ("/", Operator.DIVIDE)
    ]
)
def test_binary_expression_operator(operator, exp):
    args = {
        "line": 4,
        "operator": operator,
        "left": Expression(4),
        "right": Expression(3)
    }
    bin = BinaryExpression.generate(**args)
    assert hasattr(bin, "operator")
    assert bin.operator == exp
