import pytest

from Expressions.Expression import Expression
from Expressions.InvocationExpression import InvocationExpression
from Factories.ExpressionFactory import ExpressionFactory

@pytest.mark.parametrize(
    "input", [
        ({"line": 54, "exp": "invocation","id": "g",
          "args": [
            {"line": 54,"exp": "num","value": "1"},
            {"line": 54,"exp": "null"}
          ]
        })
    ]
)
def test_invocation_expression(input):
    expr = InvocationExpression.generate(ExpressionFactory.generate, input)
    assert len(expr.args) == 2
    assert hasattr(expr, "id")
    for arg in expr.args:
        assert isinstance(arg, Expression)
