from DeclarationFactory import DeclarationFactory as df

class FunctionFactory:

    def generate(self, line, id, parameters, return_type, declarations, body):
        declarations = df.generate(declarations)
