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

    def __init__(self, op, guard, then_label, else_label):
        super(ConditionalInstruction, self, ).__init__(op)
        self.op = op
        self.guard = guard
        self.then_label = then_label
        self.else_label = else_label

    @classmethod
    def generate(cls, code: Expression,
                 instr_mngr: InstructionsManager, factory_fn
                 ):
        op = "br i1"
        guard = cls.eval_guard(code.guard, instr_mngr, factory_fn)
        then_label = f"label {instr_mngr.current_node().successors[0]}"
        else_label = f"label {instr_mngr.current_node().successors[1]}"
        instr = ConditionalInstruction(op, guard, then_label, else_label)
        instr_mngr.add_instruction(instr)
        return instr

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

    def to_text(self):
        return f"{self.op} {self.guard.to_value()} {self.then_label} {self.else_label}"
