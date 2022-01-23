from Factories.DeclarationFactory import DeclarationFactory as df
from Factories.DeclarationFactory import type_switch
from Function import Function
from Statements.AssignmentStatement import AssignmentStatement
from Statements.ConditionalStatement import ConditionalStatement
from Statements.ReturnStatement import ReturnStatement
from Statements.Statement import Statement


class FunctionFactory:
    """
    Declarations (JSON representation) --> Locals (Function obj)
    """

    @classmethod
    def generate(cls, line, id, parameters, return_type, declarations, body):
        locals = list(map(lambda x: df.generate(**x), declarations))
        parameters = list(map(lambda x: df.generate(**x), parameters))
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
        if stmt_purpose == "return":
            return ReturnStatement.generate(stmt)
        elif stmt_purpose == "assign":
            return AssignmentStatement.generate(stmt)
        elif stmt_purpose == "if":
            then_dict = stmt.get("then")
            else_dict = stmt.get("else")
            stmt["then"] = cls.statement_switch(then_dict)
            stmt["else"] = cls.statement_switch(else_dict)
            return ConditionalStatement.generate(stmt)


