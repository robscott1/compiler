from Type import Type


class Function:

    def __init__(self, line: int, id: str, parameters: list,
                 return_type: Type, locals: list, body
                 ):
        self.line = line
        self.id = id
        self.parameters = parameters
        self.return_type = return_type
        self.locals = locals
        self.body = body

    def id_in_scope(self, id: str):
        for decl in self.locals:
            if decl.id == id:
                return True
        return self.id_is_param(id)

    def get_id_type(self, id: str):
        for param in self.parameters:
            if param.id == id:
                return param.type
        for decl in self.locals:
            if decl.id == id:
                return decl.type
        return False

    def id_is_param(self, id: str):
        for param in self.parameters:
            if param.id == id:
                return True

    def analyze(self, tc):
        for stmt in self.body:
            stmt.analyze(tc)



