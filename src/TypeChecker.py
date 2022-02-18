from BoolType import BoolType
from ControlFlowNode import ControlFlowNode
from IntType import IntType
from Factories.TypeFactory import TypeFactory as tf
from Factories.DeclarationFactory import DeclarationFactory as df
from Factories.FunctionFactory import FunctionFactory as ff

GLOBAL_FLAG = 0


class TypeChecker:

    def __init__(self, json: dict):
        self.type_map = self.build_type_map(json.get("types"))
        self.global_map = self.build_global_map(json.get("declarations"))
        self.fn_map = self.build_fn_map(json.get("functions"))
        self.current_scope = self.fn_map.get("main")
        self.control_flow = None

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
        if type_decl.id in (cls.type_map if location else cls.global_map):
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
    @classmethod
    def build_type_map(cls, types: list):
        type_map = {"int": IntType, "bool": BoolType}
        for td in types:
            t = tf.generate(td)
            type_map[t.id] = t
        return type_map

    '''
    Creates map of all global variables that get initialized under the
    Declarations key of the program. 
    
    @validations:
        - Types initialized exist (dont need to check fields yet)
        - No duplicate names
    '''
    @classmethod
    def build_global_map(cls, globals: list):
        global_map = {}
        for obj in globals:
            d = df.generate(**obj)
            global_map[d.id] = d
        return global_map

    """
    Builds map of all functions using the FunctionFactory
    
    @:param:
        - dictionary from JSON parser.
    
    @validations:
        - Proper syntax based on Statement rules and expression rules
    """
    @classmethod
    def build_fn_map(cls, funcs: list):
        fn_map = {}
        for f in funcs:
            fn = ff.generate(**f)
            fn_map[fn.id] = fn
        return fn_map

    def get_id_type(self, id: str):
        if self.current_scope.id_in_scope(id):
            return self.current_scope.get_id_type(id)
        return self.global_map.get(id).type

    def analyze(self):
        for fn in self.fn_map.values():
            self.current_scope = self.fn_map.get(fn.id)
            fn.analyze(self)

    def get_struct_field_idx(self, structure: str, field: str):
        return self.type_map.get(structure).get_field_index(field)


