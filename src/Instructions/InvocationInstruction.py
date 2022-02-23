from Expressions.Expression import Expression
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.NewExpression import NewExpression
from Expressions.NullExpression import NullExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.BitcastInstruction import BitcastInstruction
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
        instr = InvocationInstruction("call", result, type, fn_id, args)
        instr_mngr.add_instruction(instr)
        return instr

    @classmethod
    def eval_args(cls, arg: Expression,
                  instr_mngr: InstructionsManager,
                  factory_fn):
        if isinstance(arg, InvocationExpression):
            return cls.generate(arg, instr_mngr, factory_fn)
        elif isinstance(arg, IdentifierExpression):
            return instr_mngr.get(arg.id)
        elif isinstance(arg, NewExpression):
            instr = factory_fn(arg, instr_mngr)
            instr_mngr.add_instruction(instr)
            bitcast_instr = BitcastInstruction("i8*",
                                               instr.to_value(),
                                               arg.of_type(instr_mngr.type_map).to_value(1),
                                               instr_mngr.next_tmp())
            instr_mngr.add_instruction(bitcast_instr)
            return bitcast_instr
        elif not (isinstance(arg, IntExpression) \
                  or isinstance(arg, TrueExpression) \
                  or isinstance(arg, FalseExpression) \
                    or isinstance(arg, NullExpression)
        ):
            instr = factory_fn(arg, instr_mngr)
            instr_mngr.add_instruction(instr)
            return instr
        else:
            return arg

    def to_value(self):
        return f"{self.result}"

    def to_text(self):
        args = list(map(lambda x: x.to_value(), self.args))
        return f"{self.result} = call {self.type.to_value()} {self.fn_id} ({' '.join(args)})"
