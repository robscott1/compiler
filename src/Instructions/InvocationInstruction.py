from Expressions.Expression import Expression
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager


class InvocationInstruction(Instruction):

    def __init__(self, op, result: str, type: str, fn_id: str, args: []):
        super(InvocationInstruction, self).__init__(op)
        self.result = result
        self.type = type
        self.fn_id = fn_id
        self.args = args

    @classmethod
    def generate(cls, code: InvocationExpression, instr_mngr: InstructionsManager,
                 factory_fn):
        result = instr_mngr.next_tmp()
        type = code.of_type(instr_mngr.type_map)
        fn_id = code.id
        args = list(map(lambda x: cls.eval_args(x, instr_mngr, factory_fn), code.args))
        return InvocationInstruction("call", result, type, fn_id, args)

    @classmethod
    def eval_args(cls, arg: Expression,
                  instr_mngr: InstructionsManager,
                  factory_fn):
        if isinstance(arg, InvocationExpression):
            return cls.generate(arg, instr_mngr, factory_fn)
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

    def to_value(self):
        return self.result

    def to_text(self):
        args = list(map(lambda x: x.to_value(), self.args))
        return f"{self.result} = call {self.type.to_value()} {self.fn_id} ({' '.join(args)})"