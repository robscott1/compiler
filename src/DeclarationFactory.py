from src.Declaration import Declaration
from natives.Type import Type
from natives.IntType import IntType


class DeclarationFactory:
    
    def type_switch(self, type:str) -> Type:
        if type == "int":
            return IntType()
    
    def generate(self, line_num, type_str: str, id:str):
        type = self.type_switch(type_str)
        return Declaration(line_num, type, id)
