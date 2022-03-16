from Types.BoolType import BoolType
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.NewExpression import NewExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.BitcastInstruction import BitcastInstruction
from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager
from Statements.AssignmentStatement import AssignmentStatement


class LoadInstruction(Instruction):

    def __init__(self, result, type, type_cast, location):
        self.result = result
        self.type = type
        self.type_cast = type_cast
        self.location = location

    @classmethod
    def generate(cls, code: IdentifierExpression,
                 instr_mngr: InstructionsManager,
                 factory_fn):
        type = code.of_type(instr_mngr.type_map)
        location = instr_mngr.get(code.id)

        ssa_loc = instr_mngr.ssa_read_variable(location, type)
        location = ssa_loc.to_value() if not isinstance(ssa_loc, str) else ssa_loc

        return location

    def to_value(self):
        return f"{self.result}"

    def to_text(self):
        return f"{self.result} = load {self.type.to_text()}, " \
               f"{self.type.cast_up().to_text()} {self.location}"
