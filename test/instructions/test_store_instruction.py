from Expressions.BinaryExpression import BinaryExpression
from Expressions.IntExpression import IntExpression
from Factories.InstructionFactory import InstructionFactory
from InstructionsManager import InstructionsManager
from LvalueId import LvalueId
from Operator import Operator
from Statements.AssignmentStatement import AssignmentStatement


def test_load_instruction(type_checker):
    stmt = AssignmentStatement(44, LvalueId(44, "k"),
                               BinaryExpression(44, Operator.PLUS,
                                                IntExpression(44, "3"),
                                                IntExpression(44, "2")))
    instr_mngr = InstructionsManager(type_checker)
    instr_mngr.store("k", instr_mngr.next_tmp())
    instr = InstructionFactory.create_instruction(stmt, instr_mngr)
    assert instr.to_text() == "%0 = load i32*, i32** %1"