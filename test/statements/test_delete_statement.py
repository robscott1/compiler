import pytest

from Statements.DeleteStatement import DeleteStatement

@pytest.mark.parametrize(
    "stmt", [
        {"line": 44, "stmt": "delete", "exp":
            {"line": 22, "exp": "id", "id": "y"}},

    ]
)
def test_delete_statement_generation(stmt):
    stmt = DeleteStatement.generate(stmt)
    assert isinstance(stmt, DeleteStatement)