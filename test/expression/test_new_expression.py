import pytest

from CompilerError import CompilerError
from Expressions.NewExpression import NewExpression


@pytest.mark.parametrize(
    "new", [
        ({"line": 44, "id": "B"})
    ]
)
def test_new_expression_type_check(new, type_checker):
    tc = type_checker
    with pytest.raises(CompilerError) as e:
        exp = NewExpression(**new)
        exp.type_check(tc)
        assert e.code == "001"
