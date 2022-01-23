import pytest

from Expressions.Expression import Expression
from Statements.ReturnStatement import ReturnStatement
from Statements.Statement import Statement


def test_return_statement():
    line = 3
    expression = Expression(line)
    ret = ReturnStatement(line, expression)
    assert hasattr(ret, "expression")
    assert hasattr(ret, "line")
    assert isinstance(ret.__class__, Statement.__class__)

@pytest.mark.parametrize(
    "input", [
        ({"line": 12, "stmt": "return",
          "exp": {"line": 69, "exp": "num", "value": "0"}})
    ]
)
def test_return_generate(input):
    ret_stmt = ReturnStatement.generate(input)
    assert hasattr(ret_stmt, "expression")
    assert ret_stmt.expression.value == "0"
