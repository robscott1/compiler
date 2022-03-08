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

    ICMP_OPS = {"ne", "eq", "le", "lt", "ge", "gt"}

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
        type = code.of_type(instr_mngr.type_map)
        left = cls.eval_operand(code.lft, instr_mngr, factory_fn)
        right = cls.eval_operand(code.rht, instr_mngr, factory_fn)
        result = instr_mngr.next_tmp()
        instr = BinOpInstruction(op, left, right, result, type)
        instr_mngr.add_instruction(instr)
        return instr

    @classmethod
    def type_switch(cls, op):
        if op == Operator.PLUS:
            return "add", "i32"
        elif op == Operator.MINUS:
            return "sub", "i32"
        elif op == Operator.DIVIDE:
            return "sdiv", "i32"
        elif op == Operator.OR:
            return "or", "i1"
        elif op == Operator.AND:
            return "and", "i1"
        elif op == Operator.EQ:
            return "icmp eq", "i32"
        elif op == Operator.GE:
            return "icmp sge", "i32"
        elif op == Operator.GT:
            return "icmp sgt", "i32"
        elif op == Operator.LE:
            return "icmp sle", "i32"
        elif op == Operator.LT:
            return "icmp slt", "i32"
        elif op == Operator.NE:
            return "icmp ne", "i32"
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
            return instr
        else:
            return operand.to_value()

    def to_value(self):
        return f"{self.result}"

    def to_text(self):
        left = self.left if isinstance(self.left, str) else self.left.to_value()
        right = self.right if isinstance(self.right, str) else self.right.to_value()
        return f"{self.result} = {self.op} {self.type.to_text()} {left}, " \
               f"{right}"
