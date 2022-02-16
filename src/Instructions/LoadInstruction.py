from BoolType import BoolType
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager
from IntType import IntType
from Statements.AssignmentStatement import AssignmentStatement


class StoreInstruction(Instruction):

    def __init__(self, result, type, type_cast, location):
        self.result = result
        self.type = type
        self.type_cast = type_cast
        self.location = location

    @classmethod
    def generate(cls, code: AssignmentStatement,
                 instr_mngr: InstructionsManager,
                 factory_fn):
        result = instr_mngr.get(code.target.id)
        type = cls.type_switch(code.source, instr_mngr.type_map)
        location = cls.eval_source(code.source, instr_mngr, factory_fn)

        instruction = StoreInstruction(result, type, type, location)
        instr_mngr.add_instruction(instruction)
        return instruction

    @classmethod
    def type_switch(cls, source, type_map):
        t = source.of_type(type_map)
        if isinstance(t, BoolType):
            return "i1"
        else:
            return "i32"

    @classmethod
    def eval_source(cls, source, instr_mngr: InstructionsManager, factory_fn):
        if isinstance(source, IdentifierExpression):
            return instr_mngr.get(source.id)
        elif (isinstance(source, IntExpression) or \
                  isinstance(source, FalseExpression) or \
                  isinstance(source, TrueExpression)
        ):
            return source.to_value()
        else:
            instr = factory_fn(source, instr_mngr)
            instr_mngr.add_instruction(instr)
            return instr.result

    def to_text(self):
        return f"{self.result} = load {self.type}, " \
               f"{self.type}* {self.location}"
