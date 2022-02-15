from Declaration import Declaration
from Expressions.BinaryExpression import BinaryExpression
from Instructions.AllocationInstruction import AllocationInstruction
from Instructions.ArithmeticInstruction import ArithmeticInstruction
from Instructions.LoadInstruction import StoreInstruction
from IntType import IntType
from Statements.AssignmentStatement import AssignmentStatement


class InstructionFactory:

    @classmethod
    def create_instruction(cls, code, instr_mngr):
        if isinstance(code, Declaration):
            return AllocationInstruction.generate(instr_mngr, code)
        elif isinstance(code, BinaryExpression):
            return ArithmeticInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, AssignmentStatement):
            return StoreInstruction.generate(code, instr_mngr, cls.create_instruction)

        else:
            return AllocationInstruction.generate(instr_mngr,
                                                  Declaration("32", IntType(), "k"))

