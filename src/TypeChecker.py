class TypeChecker:

    def __init__(self):
        # Valid types that can be initialized
        self.types = dict()
        # Actual initialized values at the global scope,
        # should prevent mix-up with locals.
        # Can be a TypeDeclaration or Declaration
        self.globals = dict()
