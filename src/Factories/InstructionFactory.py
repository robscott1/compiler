from Declaration import Declaration
from Expressions.BinaryExpression import BinaryExpression
from Expressions.DotExpression import DotExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.NewExpression import NewExpression
from Expressions.ReadExpression import ReadExpression
from Instructions.AllocationInstruction import AllocationInstruction
from Instructions.BinOpInstruction import BinOpInstruction
from Instructions.ConditionalInstruction import ConditionalInstruction
from Instructions.DeleteInstruction import DeleteInstruction
from Instructions.DotInstruction import DotInstruction
from Instructions.InvocationInstruction import InvocationInstruction
from Instructions.JumpInstruction import JumpInstruction
from Instructions.LoadInstruction import LoadInstruction
from Instructions.NewInstruction import NewInstruction
from Instructions.PrintInstruction import PrintInstruction
from Instructions.ReadInstruction import ReadInstruction
from Instructions.ReturnInstruction import ReturnInstruction
from Instructions.StoreInstruction import StoreInstruction
from Statements.DeleteStatement import DeleteStatement
from Statements.PrintStatement import PrintStatement
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
            return DotInstruction.generate_retrieve(code, instr_mngr, cls.create_instruction)
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
        elif isinstance(code, PrintStatement):
            return PrintInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, DeleteStatement):
            return DeleteInstruction.generate(code, instr_mngr, cls.create_instruction)
        elif isinstance(code, ReadExpression):
            return ReadInstruction.generate(instr_mngr)
        elif isinstance(code, IdentifierExpression):
            return LoadInstruction.generate(code, instr_mngr, cls.create_instruction)
        else:
            return AllocationInstruction.generate(instr_mngr, code)

