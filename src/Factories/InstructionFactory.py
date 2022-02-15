from Declaration import Declaration
from Expressions.BinaryExpression import BinaryExpression
from Expressions.InvocationExpression import InvocationExpression
from Instructions.AllocationInstruction import AllocationInstruction
from Instructions.BinOpInstruction import BinOpInstruction
from Instructions.InvocationInstruction import InvocationInstruction
from Instructions.LoadInstruction import StoreInstruction
from Instructions.ReturnInstruction import ReturnInstruction
from IntType import IntType
from Statements.AssignmentStatement import AssignmentStatement
from Statements.InvocationStatement import InvocationStatement
from Statements.ReturnStatement import ReturnStatement


class InstructionFactory:

    @classmethod
    def create_instruction(cls, code, instr_mngr):
        if isinstance(code, Declaration):
            return AllocationInstruction.generate(instr_mngr, code)
        elif isinstance(code, BinaryExpression):
            return BinOpInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, AssignmentStatement):
            return StoreInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, InvocationStatement):
            return InvocationInstruction.generate(code.exp, instr_mngr, cls.create_instruction)
        elif isinstance(code, ReturnStatement):
            return ReturnInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, InvocationExpression):
            return InvocationInstruction.generate(code, instr_mngr, cls.create_instruction)

        else:
            return AllocationInstruction.generate(instr_mngr,
                                                  Declaration("32", IntType(), "k"))

