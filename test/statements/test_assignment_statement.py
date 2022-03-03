import pytest

from CompilerError import CompilerError
from Factories.ExpressionFactory import ExpressionFactory
from LvalueId import LvalueId
from Statements.AssignmentStatement import AssignmentStatement


@pytest.mark.parametrize(
    "input", [
        {"line": 44, "stmt": "assign",
         "source": {"line": 48, "exp": "num", "value": "2"},
         "target": {"line": 48, "id": "i"}
         }
    ]
)
def test_assignment_statement(input):
    asgn = AssignmentStatement.generate(input)
    assert hasattr(asgn, "target")
    assert hasattr(asgn, "source")


@pytest.mark.parametrize(
    "input", [
        {"line": 44,
         "source": {"line": 48, "exp": "num", "value": "2"},
         "target": {"line": 48, "id": "i"}
         }, {"line": 44,
             "source": {"line": 48, "exp": "new", "id": "A"},
             "target": {"line": 48, "id": "a"}
             },
        {
            "line": 44,
            "source": {"line": 44, "exp": "num", "value": "2"},
            "target": {"line": 44, "left": {"line": 33, "id": "a"}, "id": "i"}
        }

    ]
)
def test_assignment_analyze(input, type_checker):
    input["source"] = ExpressionFactory.generate(input["source"])
    input["target"] = LvalueId(input.get("line"), input.get("target").get("id"))
    asgn = AssignmentStatement(**input)
    asgn.analyze(type_checker)


@pytest.mark.parametrize(
    "input, exp_code", [
        ({"line": 44,
          "source": {"line": 48, "exp": "num", "value": "2"},
          "target": {"line": 48, "id": "zz"}
          }, "200"),
        ({"line": 44,
           "source": {"line": 48, "exp": "new", "id": "A"},
           "target": {"line": 48, "id": "j"}
           }, "201"),
        ({
            "line": 44,
            "source": {"line": 44, "exp": "num", "value": "2"},
            "target": {"line": 44, "left": {"line": 33, "id": "a"}, "id": "x"}
        }, "005")
    ]
)
def test_assignment_analyze_unhappy_path(input, exp_code, type_checker):
    input["source"] = ExpressionFactory.generate(input["source"])
    input["target"] = LvalueId(input.get("line"), input.get("target").get("id"))
    asgn = AssignmentStatement(**input)
    with pytest.raises(CompilerError) as e:
        asgn.analyze(type_checker)
        assert e.code == exp_code
