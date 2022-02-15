from Expressions.Expression import Expression
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager
from Statements.ConditionalStatement import ConditionalStatement


class ConditionalInstruction(Instruction):

    def __init__(self, op, guard):
        super(ConditionalInstruction, self,).__init__(op)
        self.op = op
        self.guard = guard


    @classmethod
    def generate(cls, code: Expression,
                 instr_mngr: InstructionsManager, factory_fn):
        op = "br i1"
        guard = cls.eval_guard(code, instr_mngr, factory_fn)

    @classmethod
    def eval_guard(cls, guard: Expression,
                   instr_mngr: InstructionsManager,
                   factory_fn
    ):
        if isinstance(guard, InvocationExpression):
            instr = factory_fn(guard, instr_mngr)
            instr_mngr.add_instruction(instr)
            return instr
        if isinstance(guard, IdentifierExpression):
            return instr_mngr.get(guard.id)
        elif not (isinstance(guard, IntExpression) \
                or isinstance(guard, TrueExpression) \
                or isinstance(guard, FalseExpression)
        ):
            instr = factory_fn(guard, instr_mngr)
            instr_mngr.add_instruction(instr)
            return instr
        else:
            return guard