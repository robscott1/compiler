from Statements.Statement import Statement


class JumpStatement(Statement):

    def __init__(self, line, jmp):
        super(JumpStatement, self).__init__(line)
        self._jmp = jmp

    def jmp_to(self):
        return self._jmp