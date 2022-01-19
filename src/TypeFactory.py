from TypeDeclaration import TypeDeclaration
from DeclarationFactory import DeclarationFactory as df
from Type import Type

class TypeFactory:

    def generate(t) -> Type:
        line = t.get("line")
        id = t.get("id")
        fields = t.get("fields")

        fields = list(map(lambda x: df.generate(**x), fields))
        return TypeDeclaration(line, id, fields)


        