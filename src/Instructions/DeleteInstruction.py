from Expressions.Expression import Expression
from Instructions.BitcastInstruction import BitcastInstruction
from Instructions.Instruction import Instruction
from Instructions.LoadInstruction import LoadInstruction
from InstructionsManager import InstructionsManager
from Statements.DeleteStatement import DeleteStatement


class DeleteInstruction(Instruction):

    def __init__(self, expression):
        self.op = "@free"
        self.expression = expression

    @classmethod
    def generate(cls, code: DeleteStatement,
                 instr_mngr: InstructionsManager,
                 factory_fn
    ):
        # Assuming this will always be IdentifierExpression
        load_instr = factory_fn(code.expression, instr_mngr)

        bitcast = cls._generate_bitcast(load_instr, instr_mngr)
        instr_mngr.add_instruction(bitcast)

        instr = DeleteInstruction(load_instr.to_value())
        instr_mngr.add_instruction(instr)

        return instr

    @classmethod
    def _generate_bitcast(cls, load_instr: LoadInstruction,
                          instr_mngr: InstructionsManager):
        args = {
            "og_type": load_instr.type,
            # Assuming expression is always IdentifierExpression
            "value": load_instr.to_value(),
            "new_type": "i8*",
            "result": instr_mngr.next_tmp()
        }

        return BitcastInstruction(**args)

    def to_text(self):
        return f"call void @free(i8* {self.expression})"


