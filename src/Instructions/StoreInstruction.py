from Expressions.Expression import Expression
from Expressions.IntExpression import IntExpression
from Expressions.NewExpression import NewExpression
from Expressions.NullExpression import NullExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.BitcastInstruction import BitcastInstruction
from Instructions.DotInstruction import DotInstruction
from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager
from LvalueId import LvalueId
from LvalueStructField import LvalueStructField
from Statements.AssignmentStatement import AssignmentStatement
from l_value import Lvalue


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
        target = cls.eval_target(code.target, instr_mngr, factory_fn)
        source = cls.eval_source(code.source, instr_mngr, factory_fn)
        ll_type = code.source.of_type(instr_mngr.type_map)

        source = source if isinstance(source, str) else source.to_value()

        instr_mngr.ssa_mngr.write_variable(target, instr_mngr.current_node(), source)

        instr = StoreInstruction(target, source, ll_type)
        instr_mngr.add_instruction(instr)

        return instr

    @classmethod
    def eval_target(cls, target: Lvalue,
                    instr_mngr: InstructionsManager,
                    factory_fn
    ):
        if isinstance(target, LvalueStructField):
            dot = DotInstruction.generate_assign(target, instr_mngr, factory_fn)
            return dot.to_value()
        else:
            return instr_mngr.get(target.get_id())

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
        return f"store {self.ll_type.to_text()} {source}, " \
               f"{self.ll_type.cast_up().to_text()} {self.target}"

