import pytest

from Expressions.BinaryExpression import BinaryExpression
from Expressions.DotExpression import DotExpression
from Expressions.IntExpression import IntExpression
from Expressions.NewExpression import NewExpression
from Expressions.ReadExpression import ReadExpression
from Factories.InstructionFactory import InstructionFactory
from InstructionsManager import InstructionsManager
from LvalueId import LvalueId
from LvalueStructField import LvalueStructField
from Operator import Operator
from Statements.AssignmentStatement import AssignmentStatement


@pytest.mark.parametrize(
    "stmt, exp", [
        (AssignmentStatement(44, LvalueId(44, "k"),
                               BinaryExpression(44, Operator.PLUS,
                                                IntExpression(44, "3"),
                                                IntExpression(44, "2"))),
         "store %t2 i32, i32* %t1"),
        (AssignmentStatement(44, LvalueId(44, "k"), IntExpression(44, '3')),
         "store 3 i32, i32* %t1"),
        (AssignmentStatement(44, LvalueId(44, "k"), ReadExpression(44)),
         "store %t0 i32, i32* %t1"),
        (AssignmentStatement(33, LvalueId(44, "k"),
                             DotExpression(44, NewExpression(44, "A"), "i")),
         "store %t4 i32, i32* %t1"),
        (AssignmentStatement(
            33, LvalueStructField(44, {"line": 22, "id": "a"}, "i"),
        IntExpression(44, "3")), "store 3 i32, i32* %t3")

    ]
)
def test_load_instruction(type_checker, stmt, exp):
    instr_mngr: InstructionsManager = InstructionsManager(type_checker)
    instr_mngr.store("k", instr_mngr.next_tmp())
    instr = InstructionFactory.create_instruction(stmt, instr_mngr)
    assert instr.to_text() == exp