from Expressions.DotExpression import DotExpression
from Expressions.Expression import Expression
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.TrueExpression import TrueExpression
from InstructionsManager import InstructionsManager


class DotInstruction:

    def __init__(self, op, struct_type, ptr_value, index, result):
        self.op = op
        self.struct_type = struct_type
        self.ptr_value = ptr_value
        self.index = index
        self.result = result

    @classmethod
    def generate(cls, code: DotExpression,
                 instr_mngr: InstructionsManager,
                 factory_fn
    ):
        op = "getelementptr"
        struct_type = code.left.of_type(instr_mngr.type_map).to_value()
        ptr_value = cls.eval_left(code.left, instr_mngr, factory_fn)
        index = cls.get_field_idx(struct_type, code.id, instr_mngr)
        result = instr_mngr.next_tmp()

        instr = DotInstruction(op, struct_type, ptr_value, index, result)

        return instr

    @classmethod
    def eval_left(cls, left: Expression,
                   instr_mngr: InstructionsManager,
                   factory_fn
    ):
        if isinstance(left, InvocationExpression):
            instr = factory_fn(left, instr_mngr)
            instr_mngr.add_instruction(instr)
            return instr
        if isinstance(left, IdentifierExpression):
            return instr_mngr.get(left.id)
        else:
            return left.to_value()

    @classmethod
    def get_field_idx(cls, struct_type: str, field: str,
                      instr_mngr: InstructionsManager):
        return instr_mngr.get_field_index(struct_type, field)

    def to_value(self):
        return self.result

    def to_text(self):
        return f"{self.op} %struct.{self.struct_type}, %struct.{self.struct_type}*" \
               f" {self.ptr_value} i1 0, i32 {self.index}"
