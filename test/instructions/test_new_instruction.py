from Expressions.NewExpression import NewExpression
from Factories.InstructionFactory import InstructionFactory
from InstructionsManager import InstructionsManager


def test_new_instruction_generation(type_checker):
    instr_mngr = InstructionsManager(type_checker)
    expr = NewExpression(44, "A")
    instruction = InstructionFactory.create_instruction(expr, instr_mngr)
    assert instruction.to_text == "%1 = call i8* @malloc(i32 4)"
