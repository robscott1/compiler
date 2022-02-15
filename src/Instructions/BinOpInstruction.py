from Expressions.BinaryExpression import BinaryExpression
from Expressions.Expression import Expression
from Expressions.FalseExpression import FalseExpression
from Expressions.IdentifierExpression import IdentifierExpression
from Expressions.IntExpression import IntExpression
from Expressions.TrueExpression import TrueExpression
from Instructions.Instruction import Instruction
from InstructionsManager import InstructionsManager
from Operator import Operator


class BinOpInstruction(Instruction):

    def __init__(self, op, left, right, result, type):
        super(BinOpInstruction, self).__init__(op)
        self.left = left
        self.right = right
        self.result = result
        self.type = type

    @classmethod
    def generate(cls, code: BinaryExpression,
                 instr_mngr: InstructionsManager,
                 factory_fn):
        op, type = cls.type_switch(code.operator)
        left = cls.eval_operand(code.lft, instr_mngr, factory_fn)
        right = cls.eval_operand(code.rht, instr_mngr, factory_fn)
        result = instr_mngr.next_tmp()
        return BinOpInstruction(op, left, right, result, type)

    @classmethod
    def type_switch(cls, op):
        if op == Operator.PLUS:
            return "add", "i32"
        elif op == Operator.MINUS:
            return "sub", "i32"
        elif op == Operator.DIVIDE:
            return "sdiv", "i32"
        elif op == Operator.OR:
            return "or", "bool"
        elif op == Operator.AND:
            return "and", "bool"
        else:
            return "mul", "i32"

    @classmethod
    def eval_operand(cls, operand: Expression,
                     instr_mngr: InstructionsManager,
                     factory_fn):
        if not (isinstance(operand, IntExpression) \
                or isinstance(operand, TrueExpression) \
                or isinstance(operand, FalseExpression)
        ):
            instr = factory_fn(operand, instr_mngr)
            instr_mngr.add_instruction(instr)
            return instr
        elif isinstance(operand, IdentifierExpression):
            return instr_mngr.get(operand.id)
        else:
            return operand

    def to_value(self):
        return f"{self.result}"

    def to_text(self):
        return f"{self.result} = {self.op} {self.type} {self.left.to_value()}, " \
               f"{self.right.to_value()}"
