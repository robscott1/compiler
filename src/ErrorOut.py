from CompilerError import CompilerError


def error_out(line, msg, code):
    c = CompilerError(line, msg, code)
    raise c
    print(c.__repr__())
    exit()
