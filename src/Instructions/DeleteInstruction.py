from Expressions.Expression import Expression
from Instructions.BitcastInstruction import BitcastInstruction
from Instructions.Instruction import Instruction
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
        expression = instr_mngr.get(code.expression.id)

        bitcast = cls._generate_bitcast(code.expression, instr_mngr)
        instr_mngr.add_instruction(bitcast)

        instr = DeleteInstruction(expression)
        instr_mngr.add_instruction(instr)

        return instr

    @classmethod
    def _generate_bitcast(cls, expression: Expression,
                          instr_mngr: InstructionsManager):
        args = {
            "og_type": expression.of_type(instr_mngr.type_map),
            # Assuming expression is always IdentifierExpression
            "value": instr_mngr.get(expression.id),
            "new_type": "i8*",
            "result": instr_mngr.next_tmp()
        }

        return BitcastInstruction(**args)

    def to_text(self):
        return f"call void @free(i8* {self.expression})"


