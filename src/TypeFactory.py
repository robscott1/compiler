from src.types.TypeDeclaration import TypeDeclaration
from src.types.Type import Type

class TypeFactory:

    def generate(t) -> Type:
        line_num = t.get("line")
        id = t.get("name")
        fields = t.get("fields")
        