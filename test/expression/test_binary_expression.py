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
        "exp": "exp",  # There is an "exp" in json. Useless here
        "operator": operator,
        "lft": Expression(4),
        "rht": Expression(3)
    }
    bin = BinaryExpression.generate(args)
    assert hasattr(bin, "operator")
    assert bin.operator == exp
