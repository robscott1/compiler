from enum import Enum

from BoolType import BoolType
from CompilerError import CompilerError
from ErrorOut import error_out
from Expressions.Expression import Expression
from IntType import IntType
from Operator import Operator


class BinaryExpression(Expression):
    def __init__(self, line: int, operator: Operator,
                 lft: Expression, rht: Expression):
        super(BinaryExpression, self).__init__(line)
        self.operator = operator
        self.lft = lft
        self.rht = rht

    def of_type(self, tc):
        returns_int = {Operator.TIMES, Operator.DIVIDE, Operator.PLUS, Operator.MINUS}
        if self.operator in returns_int:
            lft_ret = self.lft.of_type(tc)
            rht_ret = self.rht.of_type(tc)
            if not lft_ret.equals(rht_ret) or isinstance(lft_ret, BoolType):
                error_out(self.line, "BinExp", "004")
            return IntType()
        else:
            lft_ret = self.lft.of_type(tc)
            rht_ret = self.rht.of_type(tc)
            # Make sure left and right evaluate to bools
            if self.operator is Operator.OR or self.operator is Operator.AND:
                if not lft_ret.equals(rht_ret) or isinstance(lft_ret, IntType):
                    error_out(self.line, "BinExp", "004")
            # Make sure left and right match only
            elif self.operator is Operator.EQ or self.operator is Operator.NE:
                if not lft_ret.equals(rht_ret):
                    error_out(self.line, "BinExp", "004")
            # Make sure left and right evaluate to ints
            else:
                if not lft_ret.equals(rht_ret) or isinstance(lft_ret, BoolType):
                    error_out(self.line, "BinExp", "004")

            return BoolType()


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

    def to_string(self):
        return "binop"