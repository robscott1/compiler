from TypeDeclaration import TypeDeclaration
from DeclarationFactory import DeclarationFactory as df
from Type import Type


class TypeFactory:

    def generate(t) -> Type:
        line = t.get("line")
        id = t.get("id")
        fields = t.get("fields")

        declarations = []
        for field in fields:
            f_line = field.get("line")
            f_id = field.get("id")
            f_type = field.get("type")
            declarations.append(df.generate(f_line, f_id, f_type))

        return TypeDeclaration(line, id, declarations)
