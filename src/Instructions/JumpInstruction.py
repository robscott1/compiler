from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager
from Statements.JumpStatement import JumpStatement


class JumpInstruction(Instruction):

    def __init__(self, op, label):
        self.op = op
        self.label = label

    @classmethod
    def generate(cls, code: JumpStatement, instr_mngr: InstructionsManager):
        instr = JumpInstruction("br label", code.jmp_to())
        instr_mngr.add_instruction(instr)
        return instr

    def to_text(self):
        return f"{self.op} {self.label}"
