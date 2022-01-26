from Factories.DeclarationFactory import DeclarationFactory as df
from Factories.DeclarationFactory import type_switch
from Function import Function
from Statements.AssignmentStatement import AssignmentStatement
from Statements.BlockStatement import BlockStatement
from Statements.ConditionalStatement import ConditionalStatement
from Statements.InvocationStatement import InvocationStatement
from Statements.PrintStatement import PrintStatement
from Statements.ReturnStatement import ReturnStatement
from Statements.Statement import Statement
from Statements.WhileStatement import WhileStatement


class FunctionFactory:
    """
    Declarations (JSON representation) --> Locals (Function obj)
    """

    @classmethod
    def generate(cls, line, id, parameters, return_type, declarations, body):
        locals = list(map(lambda x: df.generate(**x), declarations))
        parameters = list(map(lambda x: df.generate(**x), parameters))
        body = list(map(lambda x: cls.statement_switch(x), body))
        return_type = type_switch(return_type)
        args = {
            "line": line,
            "id": id,
            "parameters": parameters,
            "return_type": return_type,
            "locals": locals,
            "body": body
        }
        return Function(**args)

    @classmethod
    def statement_switch(cls, stmt: dict) -> Statement:
        stmt_purpose = stmt.get("stmt")
        if stmt_purpose == "invocation":
            return InvocationStatement.generate(stmt)
        if stmt_purpose == "return":
            return ReturnStatement.generate(stmt)
        elif stmt_purpose == "assign":
            return AssignmentStatement.generate(stmt)
        elif stmt_purpose == "if":
            return ConditionalStatement.generate(cls.statement_switch, stmt)
        elif stmt_purpose == "block":
            return BlockStatement.generate(cls.statement_switch, stmt)
        elif stmt_purpose == "while":
            return WhileStatement.generate(cls.statement_switch, stmt)
        elif stmt_purpose == "print":
            return PrintStatement.generate(stmt)




