import pytest

from Expressions.IdentifierExpression import IdentifierExpression
from Factories.InstructionFactory import InstructionFactory
from Instructions.DeleteInstruction import DeleteInstruction
from InstructionsManager import InstructionsManager
from Statements.DeleteStatement import DeleteStatement


@pytest.mark.parametrize(
    "stmt, exp", [
        (DeleteStatement(44, IdentifierExpression(44, "x")),
         "call void @free(i8* %t1)")
    ]
)
def test_delete_instruction_gen(type_checker, stmt, exp):
    instr_mngr = InstructionsManager(type_checker)
    instr_mngr.store("x", instr_mngr.next_tmp())
    delete = DeleteInstruction.generate(
        stmt, instr_mngr, InstructionFactory.create_instruction
    )
    assert delete.to_text() == exp
