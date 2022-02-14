from Declaration import Declaration
from Instructions.AllocationInstruction import AllocationInstruction
from IntType import IntType


class InstructionFactory:

    @classmethod
    def create_instruction(cls, code, type_map, mem_mngr):
        if isinstance(code, Declaration):
            return AllocationInstruction.generate(type_map, mem_mngr, code)

        else:
            return AllocationInstruction.generate(type_map, mem_mngr,
                                                  Declaration("32", IntType(), "k"))
