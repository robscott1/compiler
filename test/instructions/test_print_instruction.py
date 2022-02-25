import pytest

from Expressions.BinaryExpression import BinaryExpression
from Expressions.DotExpression import DotExpression
from Expressions.IntExpression import IntExpression
from Expressions.NewExpression import NewExpression
from Factories.InstructionFactory import InstructionFactory
from Instructions.PrintInstruction import PrintInstruction
from InstructionsManager import InstructionsManager
from Operator import Operator
from Statements.PrintStatement import PrintStatement


@pytest.mark.parametrize(
    "stmt, exp", [
        (PrintStatement(44, IntExpression(44, '3')),
         "%0 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds "\
             "([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 3)"),
        (PrintStatement(44, BinaryExpression(44, Operator.PLUS,
            IntExpression(44, "3"), IntExpression(44, "2"))),
         "%1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds "\
             "([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %0)"),
        (PrintStatement(44, DotExpression(44, NewExpression(44, "A"), "i")),
         "%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds " \
         "([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %2)"
         )
    ]
)
def test_print_instr_gen(type_checker, stmt, exp):
    instr_mngr = InstructionsManager(type_checker)
    instr = PrintInstruction.generate(stmt, instr_mngr, InstructionFactory.create_instruction)
    assert instr.to_text() == exp