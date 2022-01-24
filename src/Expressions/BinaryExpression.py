from enum import Enum

from Expressions.Expression import Expression
from Operator import Operator


class BinaryExpression(Expression):
    def __init__(self, line: int, operator: Operator,
                 lft: Expression, rht: Expression):
        super(BinaryExpression, self).__init__(line)
        self.operator = operator
        self.lft = lft
        self.rht = rht

    @classmethod
    def generate(cls, fn, exp: dict):
        op_map = {
            "*": Operator.TIMES,
            "/": Operator.DIVIDE,
            "+": Operator.PLUS,
            "-": Operator.MINUS,
            "<": Operator.LT,
            "<=": Operator.LE,
            ">": Operator.GT,
            ">=": Operator.GE,
            "==": Operator.EQ,
            "!=": Operator.NE,
            "&&": Operator.AND,
            "||": Operator.OR
        }
        exp.pop("exp")
        exp["lft"] = fn(exp.get("lft"))
        exp["rht"] = fn(exp.get("rht"))
        exp["operator"] = op_map.get(exp["operator"])
        return BinaryExpression(**exp)


