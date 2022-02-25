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
from Statements.PrintStatement import PrintStatement


class PrintInstruction(Instruction):

    def __init__(self, content: str, newline: bool, result: str):
        self.content = content
        self.newline = newline
        self.result = result

    @classmethod
    def generate(cls, code: PrintStatement,
                 instr_mngr: InstructionsManager,
                 factory_fn
    ):
        content = cls.eval_args(code.expression, instr_mngr, factory_fn)
        result = instr_mngr.next_tmp()
        instr = PrintInstruction(content, True, result)
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
            bitcast_instr = BitcastInstruction("i8*",
                                               instr.to_value(),
                                               arg.of_type(instr_mngr.type_map),
                                               instr_mngr.next_tmp())
            instr_mngr.add_instruction(bitcast_instr)
            return bitcast_instr
        elif not (isinstance(arg, IntExpression) \
                  or isinstance(arg, TrueExpression) \
                  or isinstance(arg, FalseExpression) \
                    or isinstance(arg, NullExpression)
        ):
            instr = factory_fn(arg, instr_mngr)
            return instr
        else:
            return arg

    def to_text(self):
        content = self.content.to_value() if not isinstance(self.content, str) else self.content
        return f"{self.result} = call i32 (i8*, ...) @printf(i8* getelementptr " \
               f"inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 {content})"