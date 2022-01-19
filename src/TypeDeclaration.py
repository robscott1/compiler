class TypeDeclaration:
    
    def __init__(self, line, id, fields):
        self.line = line
        self.id = id
        self.fields = fields

    def __repr__(self):
        fields = "".join(repr(self.fields))
        return f"Type {self.id}\n{fields}"