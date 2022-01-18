from natives.TypeDeclaration import TypeDeclaration
from natives.Type import Type

class TypeFactory:

    def generate(t) -> Type:
        line_num = t.get("line")
        id = t.get("name")
        fields = t.get("fields")
        