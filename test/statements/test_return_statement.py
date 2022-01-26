import pytest

from CompilerError import CompilerError
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


@pytest.mark.parametrize(
    "input", [
        ({"line": 12, "stmt": "return",
          "exp": {"line": 69, "exp": "id", "id": "a"}})
    ]
)
def test_return_analyze(input, type_checker):
    ret_stmt = ReturnStatement.generate(input)
    ret_stmt.analyze(type_checker)

@pytest.mark.parametrize(
    "input", [
        ({"line": 12, "stmt": "return",
          "exp": {"line": 69, "exp": "num", "value": "4"}})
    ]
)
def test_return_analyze(input, type_checker):
    ret_stmt = ReturnStatement.generate(input)
    with pytest.raises(CompilerError) as e:
        ret_stmt.analyze(type_checker)
        assert e.code == "500"