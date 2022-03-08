import pytest

from Declaration import Declaration
from Instructions.AllocationInstruction import AllocationInstruction
from InstructionsManager import InstructionsManager
from Types.IntType import IntType
from Types.StructType import StructType


@pytest.mark.parametrize(
    "input, exp", [
        (Declaration(44, StructType("A"), "id"), "%t1 = alloca %struct.A*"),
        (Declaration(44, IntType(), "x"), "%t1 = alloca i32")
    ]
)
def test_allocation_instr_gen(type_checker, input, exp):
    instr_mngr = InstructionsManager(type_checker)
    instr = AllocationInstruction.generate(instr_mngr, input)
    assert instr.to_text() == exp
