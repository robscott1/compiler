from enum import Enum


class Operator(Enum):
    TIMES = "*",
    DIVIDE = "/",
    PLUS = "+",
    MINUS = "-",
    LT = "<",
    LE = "<=",
    GT = ">",
    GE = ">=",
    EQ = "==",
    NE = "!=",
    AND = "&&",
    OR = "||"

