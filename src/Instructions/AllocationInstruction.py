from Types.BoolType import BoolType
from Declaration import Declaration
from Instructions.Instruction import Instruction
from Types.IntType import IntType
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
        result = instr_mngr.next_tmp(code.id)
        type = code.type.of_type(instr_mngr.type_map)
        instr = AllocationInstruction("alloca", type, result)
        instr_mngr.store(code.id, result)
        instr_mngr.add_instruction(instr)
        return instr

    def to_text(self):
        return f"{self.result} = {self.op} {self.type.to_text()}"

    def to_value(self):
        return f"{self.result}"

    @classmethod
    def type_switch(cls, t, type_map):
        if isinstance(t.of_type(type_map), IntType):
            return "i32"
        elif isinstance(t.of_type(type_map), BoolType):
            return "i1"
        else:
            return f"%struct.{t.id}"

