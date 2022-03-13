import pytest

from ControlFlowNode import ControlFlowNode
from Expressions.TrueExpression import TrueExpression
from Factories.InstructionFactory import InstructionFactory
from InstructionsManager import InstructionsManager
from Statements.BlockStatement import BlockStatement
from Statements.ConditionalStatement import ConditionalStatement
from Statements.ReturnStatement import ReturnStatement


@pytest.mark.skip()
def test_conditional_generation(type_checker, guard, left, right, exp):
    stmt = ConditionalStatement(44, guard, left, right)
    node = ControlFlowNode.generate(set(), set(),, None
    instr_mngr = InstructionsManager(type_checker)
    node.visualize_cfg(node, None, instr_mngr)

