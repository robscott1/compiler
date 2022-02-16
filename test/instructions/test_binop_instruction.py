import pytest

from Expressions.BinaryExpression import BinaryExpression
from Expressions.FalseExpression import FalseExpression
from Expressions.IntExpression import IntExpression
from Expressions.TrueExpression import TrueExpression
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
         "%1 = add i32 %0, 2"),
        (BinaryExpression(44, Operator.OR, TrueExpression(44), FalseExpression(44)),
         FalseExpression(44), Operator.AND,
         "%1 = and i1 %0, false")

    ]
)
def test_binop_generation(type_checker, exp, operator, right, left):
    expr = BinaryExpression(44, operator, left, right)
    instr_mngr = InstructionsManager(type_checker)
    instr = InstructionFactory.create_instruction(expr, instr_mngr)
    assert instr.to_text() == exp


@pytest.mark.parametrize(
    "expr, exp", [
        (BinaryExpression(44, Operator.LT,
                          IntExpression(44, "4"),
                          IntExpression(44, "4")),
         "%0 = icmp lt i1 4, 4"),
        (BinaryExpression(44, Operator.EQ,
                          BinaryExpression(44, Operator.PLUS,
                                           IntExpression(44, "3"), IntExpression(44, "3")),
                          IntExpression(44, "4")),
         "%1 = icmp eq i1 %0, 4")
    ]
)
def test_comparison_binop(type_checker, exp, expr):
    instr_mngr = InstructionsManager(type_checker)
    instr = InstructionFactory.create_instruction(expr, instr_mngr)
    assert instr.to_text() == exp
