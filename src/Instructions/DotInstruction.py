from Expressions.DotExpression import DotExpression
from Expressions.Expression import Expression
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.InvocationExpression import InvocationExpression
from Expressions.NewExpression import NewExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.BitcastInstruction import BitcastInstruction
from Instructions.LoadInstruction import LoadInstruction
from InstructionsManager import InstructionsManager
from LvalueStructField import LvalueStructField
from Types.StructType import StructType


class DotInstruction:

    def __init__(self, op, struct_type, ptr_value, index, result):
        self.op = op
        self.struct_type = struct_type
        self.ptr_value = ptr_value
        self.index = index
        self.result = result

    @classmethod
    def generate_retrieve(cls, code: DotExpression,
                          instr_mngr: InstructionsManager,
                          factory_fn
        ):
        op = "getelementptr"
        struct_type = code.left.of_type(instr_mngr.type_map)
        ptr_value = cls.eval_left(code.left, instr_mngr, factory_fn)
        index = cls.get_field_idx(struct_type, code.id, instr_mngr)
        result = instr_mngr.next_tmp()

        instr = DotInstruction(op, struct_type, ptr_value, index, result)
        instr_mngr.add_instruction(instr)

        load_instr_param = {
            "result": instr_mngr.next_tmp(),
            "type": cls.get_field_type(struct_type, code.id, instr_mngr),
            "type_cast": cls.get_field_type(struct_type, code.id, instr_mngr),
            "location": instr.to_value()
        }

        load_instr = LoadInstruction(**load_instr_param)
        instr_mngr.add_instruction(load_instr)

        return load_instr

    @classmethod
    def generate_assign(cls, code: LvalueStructField,
                        instr_mngr: InstructionsManager,
                        factory_fn
    ):
        # TODO: load in the structure pointer to a temp
        load_type = code.get_struct_type(instr_mngr.type_map)
        load_args = {
            "result": instr_mngr.next_tmp(),
            "type": load_type,
            "type_cast": load_type,
            "location": instr_mngr.get(code.left)
        }
        load_instr = LoadInstruction(**load_args)
        instr_mngr.add_instruction(load_instr)

        # TODO: get the element pointer as part of this instruction
        struct_type = code.get_struct_type(instr_mngr.type_map)
        get_ptr_args = {
            "op": "getelementptr",
            "struct_type": struct_type,
            "ptr_value": load_instr.to_value(),
            "index": cls.get_field_idx(struct_type, code.id, instr_mngr),
            "result": instr_mngr.next_tmp()
        }
        get_instr = DotInstruction(**get_ptr_args)
        instr_mngr.add_instruction(get_instr)

        # TODO: make the to_value() poi to the result of this instruction
        #       the assignment stmt will pick it up from there and store
        # or just return this instruction to the assignment statement that
        # is using it
        return get_instr

    @classmethod
    def eval_left(cls, left: Expression,
                   instr_mngr: InstructionsManager,
                   factory_fn
    ):
        if isinstance(left, InvocationExpression)\
            or isinstance(left, IdentifierExpression
        ):
            instr = factory_fn(left, instr_mngr)
            return instr
        elif isinstance(left, NewExpression):
            instr = factory_fn(left, instr_mngr)
            bitcast_instr = BitcastInstruction("i8*",
                                               instr.to_value(),
                                               left.of_type(instr_mngr.type_map),
                                               instr_mngr.next_tmp())
            instr_mngr.add_instruction(bitcast_instr)
            return bitcast_instr.to_value()
        else:
            return left.to_value()

    @classmethod
    def get_field_idx(cls, struct_type: StructType, field: str,
                      instr_mngr: InstructionsManager):
        return instr_mngr.get_field_index(struct_type.id, field)

    @classmethod
    def get_field_type(cls, struct_type: StructType, field: str,
                       instr_mngr: InstructionsManager):
        return instr_mngr.get_field_type(struct_type.id, field)

    def to_value(self):
        return f"{self.result}"

    def to_text(self):
        ptr_value = self.ptr_value if isinstance(self.ptr_value, str) \
                                        else self.ptr_value.to_value()
        return f"{self.result} = " \
               f"{self.op} {self.struct_type.to_llvm_type()}, {self.struct_type.to_text()}" \
               f" {ptr_value}, i32 0, i32 {self.index}"
