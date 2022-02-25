from Expressions.NewExpression import NewExpression
from Instructions.BitcastInstruction import BitcastInstruction
from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager


class NewInstruction(Instruction):

    def __init__(self, op, lib_fn: str,
                 exp_type_return: str,
                 args: str, result):
        self.op = op
        self.lib_fn = lib_fn
        self.exp_type_return = exp_type_return
        self.args = args
        self.result = result

    @classmethod
    def generate(cls, code: NewExpression,
                 instr_mngr: InstructionsManager,
                 factory_fn
    ):
        op = "call"
        lib_fn = "@malloc"
        bytes_allocated = instr_mngr.get_mem_size(code.id)
        exp_type_return = "i8*"
        args = f"(i32 {bytes_allocated})"
        result = instr_mngr.next_tmp()

        instr = NewInstruction(op, lib_fn, exp_type_return, args, result)
        instr_mngr.add_instruction(instr)

        return instr

    def to_value(self):
        return f"{self.result}"

    def to_text(self):
        return f"{self.result} = {self.op} {self.exp_type_return} " \
               f"{self.lib_fn}{self.args}"

