import pytest

from CompilerError import CompilerError
from Factories.FunctionFactory import FunctionFactory
from Statements.AssignmentStatement import AssignmentStatement
from Statements.ConditionalStatement import ConditionalStatement
from Statements.ReturnStatement import ReturnStatement


@pytest.mark.parametrize(
    "input", [
        ({
            "line": 54,
            "stmt": "if",
            "guard": {
                "line": 54,
                "exp": "binary",
                "operator": ">=",
                "lft": {"line": 48, "exp": "num", "value": "2"},
                "rht": {"line": 48, "exp": "num", "value": "2"}
            },
            "then": {
                "stmt": "assign",
                "source": {"line": 48, "exp": "num", "value": "2"},
                "target": {"line": 48, "id": "i"}},
            "else": {"stmt": "return",
                     "exp": {"line": 69, "exp": "num", "value": "0"}}
        })
    ]
)
def test_test_conditional_statement_generate(input):
    stmt = ConditionalStatement.generate(
        FunctionFactory.statement_switch, input)
    assert hasattr(stmt, "guard")
    assert hasattr(stmt, "then_block")
    assert stmt.then_block.__class__ == AssignmentStatement
    assert stmt.else_block.__class__ == ReturnStatement


@pytest.mark.parametrize(
    "input", [{
        "line": 54,
        "stmt": "if",
        "guard": {
            "line": 54,
            "exp": "binary",
            "operator": ">=",
            "lft": {"line": 48, "exp": "num", "value": "2"},
            "rht": {"line": 48, "exp": "num", "value": "2"}
        },
        "then": {
            "stmt": "assign",
            "source": {"line": 48, "exp": "num", "value": "2"},
            "target": {"line": 48, "id": "i"}},
        "else": {"stmt": "assign",
                 "source": {"line": 48, "exp": "num", "value": "2"},
                 "target": {"line": 48, "id": "i"}}
    }, {
        "line": 54,
        "stmt": "if",
        "guard": {
            "line": 54,
            "exp": "binary",
            "operator": "||",
            "lft": {"line": 48, "exp": "true"},
            "rht": {"line": 48, "exp": "true"}
        },
        "then": {
            "stmt": "assign",
            "source": {"line": 48, "exp": "num", "value": "2"},
            "target": {"line": 48, "id": "i"}},
        "else": {"stmt": "assign",
                 "source": {"line": 48, "exp": "num", "value": "2"},
                 "target": {"line": 48, "id": "i"}}
    }
    ]
)
def test_analyze(input, type_checker):
    stmt = ConditionalStatement.generate(
        FunctionFactory.statement_switch, input)
    stmt.analyze(type_checker)

@pytest.mark.parametrize(
    "input", [{
        "line": 54,
        "stmt": "if",
        "guard": {
            "line": 54,
            "exp": "binary",
            "operator": "||",
            "lft": {"line": 48, "exp": "num", "value": "2"},
            "rht": {"line": 48, "exp": "num", "value": "2"}
        },
        "then": {
            "stmt": "assign",
            "source": {"line": 48, "exp": "num", "value": "2"},
            "target": {"line": 48, "id": "i"}},
        "else": {"stmt": "assign",
                 "source": {"line": 48, "exp": "num", "value": "2"},
                 "target": {"line": 48, "id": "i"}}
    }, {
        "line": 54,
        "stmt": "if",
        "guard": {
            "line": 54,
            "exp": "binary",
            "operator": "*",
            "lft": {"line": 48, "exp": "true"},
            "rht": {"line": 48, "exp": "true"}
        },
        "then": {
            "stmt": "assign",
            "source": {"line": 48, "exp": "num", "value": "2"},
            "target": {"line": 48, "id": "i"}},
        "else": {"stmt": "assign",
                 "source": {"line": 48, "exp": "num", "value": "2"},
                 "target": {"line": 48, "id": "i"}}
    }]
)
def test_analyze_unhappy_path(input, type_checker):
    stmt = ConditionalStatement.generate(
        FunctionFactory.statement_switch, input)
    with pytest.raises(CompilerError) as e:
        stmt.analyze(type_checker)
        assert e.code == "100"
