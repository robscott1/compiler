class TypeChecker:

    def __init__(self):
        # Valid types that can be initialized
        self.types = dict()
        # Actual initialized values at the global scope,
        # should prevent mix-up with locals.
        # Can be a TypeDeclaration or Declaration
        self.globals = dict()

    '''
    Checks to make sure there is not a Type with the same name.
    Global initialization will have further checks.
    '''
    def check_type_decl(self, type_decl):
        if id in self.types:
            print(f"Error: Type {type_decl.id} has already been defined.")
            exit()
        
