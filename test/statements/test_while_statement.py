import pytest

from Expressions.Expression import Expression
from Factories.FunctionFactory import FunctionFactory
from Statements.Statement import Statement
from Statements.WhileStatement import WhileStatement

@pytest.mark.parametrize(
    "input", [
        ({"line": 62, "stmt": "while", "guard": {
            "line": 62, "exp": "true"},
          "body": {"stmt": "block", "list": [{
            "line": 64, "stmt": "print",
            "exp": {"line": 64, "exp": "num", "value": "7"},
            "endl": False
          }]}
        })
    ]
)
def test_while_statement(input):
    stmt = WhileStatement.generate(FunctionFactory.statement_switch, input)
    assert isinstance(stmt, Statement)
    assert isinstance(stmt.guard, Expression)
