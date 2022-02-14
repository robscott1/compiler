from Declaration import Declaration
from Instructions.Instruction import Instruction
from IntType import IntType
from TemporaryMemoryManager import TemporaryMemoryManager


class AllocationInstruction(Instruction):

    def __init__(self, op, type, result):
        super(AllocationInstruction, self).__init__(op)
        self.type = type
        self.result = result

    @classmethod
    def generate(cls, type_map, mem_mngr: TemporaryMemoryManager, code: Declaration):
        result = mem_mngr.next_tmp()
        type = cls.type_switch(code.type)
        return AllocationInstruction("alloca", type, result)

    def to_text(self):
        return f"{self.result} = {self.op} {self.type}"

    @classmethod
    def type_switch(cls, t):
        if isinstance(t, IntType):
            return "i32"

