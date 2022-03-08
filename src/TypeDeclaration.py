from Types.BoolType import BoolType
from ErrorOut import error_out
from Types.IntType import IntType
from Type import Type


class TypeDeclaration(Type):

    """
    @param:
        - line (int): line number
        - id (str): id of struct
        - fields (Declaration): fields of structure
    """
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

    def get_mem_size(self):
        total_bytes = 0
        for declaration in self.fields:
            if (isinstance(declaration.type, IntType)) or \
                    (isinstance(declaration.type, BoolType)):
                total_bytes += 4
            else:
                total_bytes += 1

        return f"{total_bytes}"

    def to_text(self):
        return f"%struct.{self.id} = " \
               f"type {{ {', '.join(list(map(lambda x: x.to_llvm_type(), self.fields)))}" \
               f" }}"

    def to_llvm_type(self):
        return f"%struct.{self.id}"

