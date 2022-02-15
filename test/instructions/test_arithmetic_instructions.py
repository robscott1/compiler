import pytest

from Expressions.BinaryExpression import BinaryExpression
from Expressions.IntExpression import IntExpression
from Factories.InstructionFactory import InstructionFactory
from InstructionsManager import InstructionsManager
from Operator import Operator


@pytest.mark.parametrize(
    "left, right, operator, exp",
    [
        (IntExpression(44, "3"), IntExpression(44, "2"),
         Operator.PLUS, "%0 = add i32 3, 2"),
        (BinaryExpression(44, Operator.PLUS, IntExpression(44, "3"), IntExpression(44, "2")),
         IntExpression(44, "2"), Operator.PLUS,
         "%1 = add i32 %0, 2")

    ]
)
def test_arithmetic_generation(type_checker, exp, operator, right, left):
    expr = BinaryExpression(44, operator, left, right)
    instr_mngr = InstructionsManager(type_checker)
    instr = InstructionFactory.create_instruction(expr, instr_mngr)
    assert instr.to_text() == exp
