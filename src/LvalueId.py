from l_value import Lvalue


class LvalueId(Lvalue):

    def __init__(self, line: int, id: str):
        super(LvalueId, self).__init__()
        self.line = line
        self.id = id

