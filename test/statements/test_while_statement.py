import pytest

from CompilerError import CompilerError
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
def test_while_statement(input, type_checker):
    stmt = WhileStatement.generate(FunctionFactory.statement_switch, input)
    stmt.analyze(type_checker)

@pytest.mark.parametrize(
    "input", [
        ({"line": 62, "stmt": "while", "guard": {
            "line": 62, "exp": "num", "value": "4"},
          "body": {"stmt": "block", "list": [{
            "line": 64, "stmt": "print",
            "exp": {"line": 64, "exp": "num", "value": "7"},
            "endl": False
          }]}
        })
    ]
)
def test_while_statement_unhappy_path(input, type_checker):
    stmt = WhileStatement.generate(FunctionFactory.statement_switch, input)
    with pytest.raises(CompilerError) as e:
        stmt.analyze(type_checker)
        assert e.code == "600"