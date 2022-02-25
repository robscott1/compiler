from Declaration import Declaration
from Expressions.BinaryExpression import BinaryExpression
from Expressions.DotExpression import DotExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.NewExpression import NewExpression
from Instructions.AllocationInstruction import AllocationInstruction
from Instructions.BinOpInstruction import BinOpInstruction
from Instructions.ConditionalInstruction import ConditionalInstruction
from Instructions.DotInstruction import DotInstruction
from Instructions.InvocationInstruction import InvocationInstruction
from Instructions.JumpInstruction import JumpInstruction
from Instructions.LoadInstruction import LoadInstruction
from Instructions.NewInstruction import NewInstruction
from Instructions.ReturnInstruction import ReturnInstruction
from Types.IntType import IntType
from Statements.AssignmentStatement import AssignmentStatement
from Statements.BlockStatement import BlockStatement
from Statements.ConditionalStatement import ConditionalStatement
from Statements.InvocationStatement import InvocationStatement
from Statements.JumpStatement import JumpStatement
from Statements.ReturnStatement import ReturnStatement
from Statements.WhileStatement import WhileStatement


class InstructionFactory:

    @classmethod
    def create_instruction(cls, code, instr_mngr):
        if isinstance(code, Declaration):
            return AllocationInstruction.generate(instr_mngr, code)
        elif isinstance(code, DotExpression):
            return DotInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, BinaryExpression):
            return BinOpInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, AssignmentStatement):
            return LoadInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, InvocationStatement):
            return InvocationInstruction.generate(code.exp, instr_mngr, cls.create_instruction)
        elif isinstance(code, ReturnStatement):
            return ReturnInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, InvocationExpression):
            return InvocationInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, ConditionalStatement):
            return ConditionalInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, WhileStatement):
            return ConditionalInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, JumpStatement):
            return JumpInstruction.generate(code, instr_mngr)
        elif isinstance(code, NewExpression):
            return NewInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, BlockStatement):
            for stmt in code.statements:
                cls.create_instruction(stmt, instr_mngr)
        else:
            return AllocationInstruction.generate(instr_mngr,
                                                  Declaration("32", IntType(), "k"))

