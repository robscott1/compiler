from src.BoolType import BoolType
from src.IntType import IntType
from src.TypeFactory import TypeFactory as tf


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
    
    @validations:
        - No duplicate names
        - Does not start with a number
        - Any Types in each Declaration are valid
    '''

    def check_type_decl(cls, type_decl):
        if type_decl.id in cls.type_map:
            return False
        if type_decl.id[0].isnumeric():
            return False
        return True

    '''
    Creates a map of TypeDeclaration objects with Declarations for 
    each field (if applicable). Needs to pass along the working map
    to the TypeFactory, then subsequently the Declaration factory.
    '''

    def build_type_map(self, json):
        for td in json.get("types"):
            t = tf.generate(td, self.type_map)
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
        return {}