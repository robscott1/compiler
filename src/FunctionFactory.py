from DeclarationFactory import DeclarationFactory as df
from DeclarationFactory import type_switch
from Function import Function

class FunctionFactory:

    def generate(self, line, id, parameters, return_type, locals, body):
        locals = list(map(lambda x: df.generate(**x), locals))
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
