from Expressions.Expression import Expression
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager
from Statements.ReturnStatement import ReturnStatement


class ReturnInstruction(Instruction):

    def __init__(self, op, type, value):
        super(ReturnInstruction, self).__init__(op)
        self.type = type
        self.value = value

    @classmethod
    def generate(cls, code: ReturnStatement,
                 instr_mngr: InstructionsManager, factory_fn):
        type = code.expression.of_type(instr_mngr.type_map)
        value = cls.eval_value(code.expression, instr_mngr, factory_fn).to_value()
        return ReturnInstruction("ret", type, value)

    @classmethod
    def eval_value(cls, arg: Expression,
                  instr_mngr: InstructionsManager,
                  factory_fn):
        if isinstance(arg, InvocationExpression):
            return factory_fn(arg, instr_mngr)
        if isinstance(arg, IdentifierExpression):
            return instr_mngr.get(arg.id)
        elif not (isinstance(arg, IntExpression) \
                or isinstance(arg, TrueExpression) \
                or isinstance(arg, FalseExpression)
        ):
            instr = factory_fn(arg, instr_mngr)
            instr_mngr.add_instruction(instr)
            return instr
        else:
            return arg

    def to_text(self):
        if self.value == "void":
            return "ret void"
        else:
            return f"ret {self.type.to_value()} {self.value}"