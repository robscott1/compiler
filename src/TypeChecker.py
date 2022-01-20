from src.BoolType import BoolType
from src.IntType import IntType
from src.TypeFactory import TypeFactory as tf
from src.DeclarationFactory import DeclarationFactory as df

GLOBAL_FLAG = 0


class TypeChecker:

    def __init__(self):
        self.type_map = {
            "int": IntType,
            "bool": BoolType,
        }
        self.globals = {}

    '''
    Checks to make sure there is not a Type with the same name.
    Global initialization will have further checks. 
    @:parameters:
        - type_decl: a TypeDeclaration
        - location: (int) Identifies if the evaluation is for a type or decl
            - 1: type, 0: declaration
    
    @validations:
        - No duplicate names
        - Does not start with a number
        - Any Types in each Declaration are valid
    '''

    def check_type_decl_or_global(cls, type_decl, location):
        if type_decl.id in (cls.type_map if location else cls.globals):
            raise Exception("Duplicate name error.")
        if type_decl.type not in cls.type_map:
            raise Exception("Undeclared type reference.")
        if type_decl.id[0].isnumeric():
            raise Exception("Name error.")

    '''
    Creates a map of TypeDeclaration objects with Declarations for 
    each field (if applicable). Needs to pass along the working map
    to the TypeFactory, then subsequently the Declaration factory.
    '''

    def build_type_map(self, json):
        for td in json.get("types"):
            t = tf.generate(td)
            self.type_map[t.id] = t
        print(self.type_map)
        return self.type_map

    '''
    Creates map of all global variables that get initialized under the
    Declarations key of the program. 
    
    @validations:
        - Types initialized exist (dont need to check fields yet)
        - No duplicate names
    '''
    def build_global_map(self, json):
        for obj in json.get("declarations"):
            d = df.generate(**obj)
            self.check_type_decl_or_global(d, GLOBAL_FLAG)
            self.globals[d.id] = d
        return self.globals

