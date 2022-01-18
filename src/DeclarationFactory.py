from src.Declaration import Declaration
from src.Type import Type
from src.IntType import IntType


class DeclarationFactory:
    
    def type_switch(self, type:str) -> Type:
        if type == "int":
            return IntType()
    
    def generate(self, line_num, type_str: str, id:str):
        type = self.type_switch(type_str)
        return Declaration(line_num, type, id)
