import pytest

from Expressions.InvocationExpression import InvocationExpression
from Factories.FunctionFactory import FunctionFactory
from Statements.InvocationStatement import InvocationStatement


@pytest.mark.parametrize(
    "input", [
        {
      "line": 66,"stmt": "invocation","id": "f",
      "args": [
        {
          "line": 66,"exp": "invocation", "id": "g","args": [
            {"line": 66,"exp": "num","value": "1"},
            { "line": 66,"exp": "new","id": "B"}
          ]
        }, {"line": 66,"exp": "num","value": "2"},
        {"line": 66,"exp": "new","id": "B"}
      ]}]
)
def test_invocation_statement(input):
    inv = FunctionFactory.statement_switch(input)
    assert hasattr(inv, "exp")
    assert isinstance(inv.exp, InvocationExpression)

@pytest.mark.parametrize(
    "input", [{
      "line": 66,"stmt": "invocation", "id": "f",
      "args": [
        {"line": 66, "exp": "num", "value": "2"},
        {"line": 66, "exp": "false"}
      ]}]
)
def test_invocation_statement_analyze(input, type_checker):
    inv = InvocationStatement.generate(input)
    inv.analyze(type_checker)