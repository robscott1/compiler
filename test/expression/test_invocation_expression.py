import pytest

from Expressions.Expression import Expression
from Expressions.InvocationExpression import InvocationExpression
from Factories.ExpressionFactory import ExpressionFactory


@pytest.mark.parametrize(
    "input, exp_args", [
        ({"line": 54, "exp": "invocation", "id": "g",
          "args": [
              {"line": 54, "exp": "num", "value": "1"},
              {"line": 54, "exp": "null"}
          ]
          }, 2),
        ({"line": 54, "exp": "invocation", "id": "g",
          "args": [
              {"line": 54, "exp": "dot", "left":
                  {"line": 54, "exp": "invocation", "id": "g",
                   "args": [
                       {"line": 54, "exp": "num", "value": "1"},
                       {"line": 54, "exp": "null"}
                   ]
                   }, "id": "f"
               },
          ]}, 1)
    ]
)
def test_invocation_expression(input, exp_args):
    expr = InvocationExpression.generate(ExpressionFactory.generate, input)
    assert len(expr.args) == exp_args
    assert hasattr(expr, "id")
    for arg in expr.args:
        assert isinstance(arg, Expression)

