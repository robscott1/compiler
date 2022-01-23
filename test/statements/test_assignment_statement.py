import pytest

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
