import pytest

from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.TrueExpression import TrueExpression
from Factories.InstructionFactory import InstructionFactory
from InstructionsManager import InstructionsManager
from Statements.InvocationStatement import InvocationStatement


@pytest.mark.parametrize(
    "expr, exp", [
        # !!! This "f" fn lives with type_checker fixture
        (InvocationExpression(44, "f", [IntExpression(44, "2")]),
         "%1 = call i32 f (2)"),
        (InvocationExpression(44, "f", [IntExpression(44, "2"), (TrueExpression(44))]),
         "%1 = call i32 f (2 true)"),
        (InvocationExpression(44, "f", [
            InvocationExpression(44, "f", [IntExpression(44, 4), IntExpression(44, "2")]),
            (IntExpression(44, "2"))]),
         "%1 = call i32 f (%2 2)")
    ]
)
def test_invocation_instruction(type_checker, exp, expr):
    stmt = InvocationStatement(44, expr)
    instr_mngr = InstructionsManager(type_checker)
    instr = InstructionFactory.create_instruction(stmt, instr_mngr)
    assert instr.to_text() == exp