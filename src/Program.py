STANDARD_GLOBALS = [
    "\n@.str = private unnamed_addr constant [3 x i8] c\"%d\\00\"",
    "@.str.1 = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"",
    "@READ_MEM = common global i32 0",

]

STANDARD_FUNCS = [
    "\ndeclare dso_local void @free(i8*) #1",
    "declare dso_local i32 @printf(i8*, ...) #1",
    "declare dso_local i8* @malloc(i32) #1",
    "declare dso_local i32 @__isoc99__scanf(i8*, ...) #1"
]

class Program:

    def __init__(self, tc):
        self._tc = tc
        self._types = tc.type_map
        self._globals = tc.global_map
        self._functions = tc.fn_map

    def print_program(self):
        types = "\n".join(self.get_types())
        globals = "\n".join(self.get_globals())
        functions = "\n".join(self.get_functions())
        stdlib_includes = "\n".join(STANDARD_FUNCS)

        return f"{types}\n{globals}\n{functions}\n{stdlib_includes}"

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
        return globals + STANDARD_GLOBALS

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


