from Expressions.Expression import Expression
from Expressions.IntExpression import IntExpression
from Expressions.NewExpression import NewExpression
from Expressions.NullExpression import NullExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.BitcastInstruction import BitcastInstruction
from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager
from Statements.AssignmentStatement import AssignmentStatement


class StoreInstruction(Instruction):

    def __init__(self, target, source, ll_type):
        self.target = target
        self.source = source
        self.ll_type = ll_type

    @classmethod
    def generate(cls, code: AssignmentStatement,
                 instr_mngr: InstructionsManager,
                 factory_fn
    ):
        target = instr_mngr.get(code.target.get_id())
        source = cls.eval_source(code.source, instr_mngr, factory_fn)
        ll_type = code.source.of_type(instr_mngr.type_map)

        instr = StoreInstruction(target, source, ll_type)
        instr_mngr.add_instruction(instr)

        return instr

    @classmethod
    def eval_source(cls, source: Expression,
                    instr_mngr: InstructionsManager,
                    factory_fn
    ):
        if (isinstance(source, IntExpression) \
            or isinstance(source, TrueExpression) \
            or isinstance(source, IntExpression) \
            or isinstance(source, NullExpression)
        ):
            return source
        elif isinstance(source, NewExpression):
            instr = factory_fn(source, instr_mngr)
            bitcast_instr = BitcastInstruction("i8*",
                                               instr.to_value(),
                                               source.of_type(instr_mngr.type_map),
                                               instr_mngr.next_tmp())
            instr_mngr.add_instruction(bitcast_instr)
            return bitcast_instr.to_value()
        else:
            instr = factory_fn(source, instr_mngr)
            return instr


    def to_text(self):
        source = self.source if isinstance(self.source, str) else self.source.to_value()
        type = self.ll_type if isinstance(self.ll_type, str) else self.ll_type.to_llvm_type()
        return f"store {source} {type}, {type}* {self.target}"

