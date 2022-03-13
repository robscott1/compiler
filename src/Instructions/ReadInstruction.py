from Instructions.Instruction import Instruction
from Instructions.LoadInstruction import LoadInstruction
from InstructionsManager import InstructionsManager
from Types.IntType import IntType


class ReadInstruction(Instruction):


    def __init__(self, global_read_ptr, read_success):
        self.global_read_ptr = global_read_ptr
        self.read_success = read_success

    @classmethod
    def generate(cls, instr_mngr: InstructionsManager):
        read_success = instr_mngr.next_tmp()
        instr = ReadInstruction(instr_mngr.get("@READ_MEM"),
                                read_success)

        instr_mngr.add_instruction(instr)

        load_instr_param = {
            "result": instr_mngr.next_tmp(),
            "type": IntType(),
            "type_cast": IntType(),
            "location": instr_mngr.get("@READ_MEM")
        }

        load_instr = LoadInstruction(**load_instr_param)
        instr_mngr.add_instruction(load_instr)

        return load_instr

    def to_text(self):
        return f"{self.read_success} = call i32 (i8*, ...) @__isoc99__scanf" \
               f"(i8* getelementptr([4 x i8], [4 x i8]* @.str.1, " \
               f"i32 0, i32 0), i32* {self.global_read_ptr})"

    def to_value(self):
        return f"{self.global_read_ptr}"
