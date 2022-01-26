import pytest

from CompilerError import CompilerError
from Statements.BlockStatement import BlockStatement
from Factories.FunctionFactory import FunctionFactory as ff, FunctionFactory


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

@pytest.mark.parametrize(
    "input", [
        ({"stmt": "block" ,"list": [{
            "line": 27 ,"stmt": "return" ,"exp": {
              "line": 27 ,"exp": "id" ,"id": "a"
        }}]})
    ]
)
def test_analyze(input, type_checker):
    bs = BlockStatement.generate(FunctionFactory.statement_switch, input)
    bs.analyze(type_checker)

@pytest.mark.parametrize(
    "input", [
        ({"stmt": "block" ,"list": [{
            "line": 27 ,"stmt": "return" ,"exp": {
              "line": 27 ,"exp": "num" , "value": "4"
        }}]})
    ]
)
def test_analyze_unhappy(input, type_checker):
    bs = BlockStatement.generate(FunctionFactory.statement_switch, input)
    with pytest.raises(CompilerError) as e:
        bs.analyze(type_checker)
        assert e.code == "500"