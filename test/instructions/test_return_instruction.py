import pytest

from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.TrueExpression import TrueExpression
from Factories.InstructionFactory import InstructionFactory
from InstructionsManager import InstructionsManager
from Statements.InvocationStatement import InvocationStatement
from Statements.ReturnStatement import ReturnStatement


@pytest.mark.parametrize(
    "stmt, exp", [
        (ReturnStatement(44, IntExpression(44, "4")),
         "ret i32 4"),
        (ReturnStatement(44, InvocationExpression(44, "f",
            [IntExpression(44, "2"), (TrueExpression(44))])),
        "ret i32 %0")

    ]
)
def test_return_instruction(type_checker, exp, stmt):
    instr_mngr = InstructionsManager(type_checker)
    instr = InstructionFactory.create_instruction(stmt, instr_mngr)
    assert instr.to_text() == exp