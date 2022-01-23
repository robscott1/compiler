from Factories.DeclarationFactory import DeclarationFactory as df
from Factories.DeclarationFactory import type_switch
from Function import Function
from Statements.ReturnStatement import ReturnStatement


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
    def statement_switch(cls, stmt: dict):
        stmt_purpose = stmt.get("stmt")
        if stmt_purpose == "return":
            ReturnStatement.generate(stmt)
        elif stmt_purpose == "assign":
            AssignmentStatement.generate(stmt)


