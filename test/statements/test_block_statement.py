import pytest

from Statements.BlockStatement import BlockStatement
from Factories.FunctionFactory import FunctionFactory as ff


@pytest.mark.parametrize(
    "input", [
        ({"stmt": "block", "list": [
            {"line": 56, "stmt": "return",
             "exp": {"line": 56, "exp": "num", "value": "1"},
             "endl": False}]})
    ]
)
def test_block_statement(input):
    blk_stmt = BlockStatement.generate(ff.statement_switch, input)
    assert hasattr(blk_stmt, "statements")
    assert len(blk_stmt.statements) == 1
