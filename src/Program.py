class Program:

    def __init__(self, tc):
        self._tc = tc
        self._types = tc.type_map
        self._globals = tc.global_map
        self._functions = tc.fn_map

    def print_program(self):
        types = self.get_types()
        globals = self.get_globals()
        functions = self.get_functions()

        print("\n".join(types))
        print("\n".join(globals))
        print("\n".join(functions))

    """
    get_types
    
    Will return a list of strings that represent the types declarations
    """
    def get_types(self):
        types = []
        lst = list(self._types.values())[2:]
        for t in lst:
            types.append(t.to_text())
        return types

    """
    get_globals
    
    Returns list of strings that represent the global variables
    """
    def get_globals(self):
        globals = []
        for d in self._globals.values():
            globals.append(d.to_global_declaration())
        return globals

    """
    get_functions
    
    Returns list of entry control flow nodes that contain instrions
    """
    def get_functions(self):
        functions = []
        for f in self._functions.values():
            llvm = f.llvm_representation(self._tc)
            functions.append(llvm)

        return functions


