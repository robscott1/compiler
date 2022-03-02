import pytest

from Expressions.ReadExpression import ReadExpression
from Factories.ExpressionFactory import ExpressionFactory

@pytest.mark.parametrize(
    "data", [
        {"line": 10, "exp": "read"}
    ]
)
def test_read_instruction(data):
    exp = ExpressionFactory.generate(data)
    assert isinstance(exp, ReadExpression)
