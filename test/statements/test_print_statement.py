import pytest

from Expressions.Expression import Expression
from Statements.PrintStatement import PrintStatement

@pytest.mark.parametrize(
    "input", [
        ({"line": 51, "stmt": "print",
          "exp": {"line": 51, "exp": "num", "value": "1"}
        })
    ]
)
def test_print_statement(input):
    stmt = PrintStatement.generate(input)
    assert hasattr(stmt, "expression")
    assert isinstance(stmt.expression, Expression)
