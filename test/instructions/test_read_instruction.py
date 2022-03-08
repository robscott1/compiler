import pytest

from Expressions.ReadExpression import ReadExpression
from Instructions.ReadInstruction import ReadInstruction
from InstructionsManager import InstructionsManager


@pytest.mark.parametrize(
    "exp, expected_str, expected_val",[
        (ReadExpression(44),
         "%t1 = (i8* ...) @__isoc99__scanf" \
               f"(i8* getelementptr([4 x i8], [4 x i8]* @.str.1, " \
               f"i32 0, i32 0) i32 %t0)",
         "%t0")
    ]
)
def test_read_instruction(type_checker, exp, expected_str, expected_val):
    instr_mngr = InstructionsManager(type_checker)
    instr = ReadInstruction.generate(instr_mngr)

    assert instr.to_text() == expected_str
    assert instr.to_value() == expected_val