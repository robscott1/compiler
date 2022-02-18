from CompilerError import CompilerError
from ErrorOut import error_out
from Type import Type


class TypeDeclaration(Type):
    
    def __init__(self, line, id, fields):
        self.line = line
        self.id = id
        self.fields = fields

    def __repr__(self):
        fields = "".join(repr(self.fields))
        return f"Type {self.id}\n{fields}"

    def get_field_type(self, target):
        for field in self.fields:
            if field.id == target:
                return field.type
        error_out(self.line,
                            f"Undeclared field within {self.id}",
                            code="005")

    def get_field_index(self, field):
        for i in range(len(self.fields)):
            f = self.fields[i]
            if f.id == field:
                return i
