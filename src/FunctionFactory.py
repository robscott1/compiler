from DeclarationFactory import DeclarationFactory as df
from DeclarationFactory import type_switch
from Function import Function

class FunctionFactory:

    '''
    Declarations (JSON representation) --> Locals (Function obj)
    '''
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
