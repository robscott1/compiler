from BoolType import BoolType
from Declaration import Declaration
from Instructions.Instruction import Instruction
from IntType import IntType
from InstructionsManager import InstructionsManager


class AllocationInstruction(Instruction):

    def __init__(self, op, type, result):
        super(AllocationInstruction, self).__init__(op)
        self.type = type
        self.result = result

    """
    generate
    Turns arguments to llvm instruction after a bit of prep work.
    
    @returns: AllocationInstruction
    @params:
        - type_map: for types in structs
        - instr_mngr: to allocate temporary space
        - code: the statement that will be converted to llvm
    
    """
    @classmethod
    def generate(cls, instr_mngr: InstructionsManager, code: Declaration):
        result = instr_mngr.next_tmp()
        type = cls.type_switch(code.type)
        instr = AllocationInstruction("alloca", type, result)
        instr_mngr.store(code.id, result)
        instr_mngr.add_instruction(instr)
        return instr

    def to_text(self):
        return f"{self.result} = {self.op} {self.type}"

    def to_value(self):
        return f"{self.result}"

    @classmethod
    def type_switch(cls, t):
        if t == "int":
            return "i32"
        elif t == "bool":
            return "bool"

