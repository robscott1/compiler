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
