from l_value import Lvalue


class LvalueId(Lvalue):

    def __init__(self, line: int, id: str) -> object:
        super(LvalueId, self).__init__()
        self.line = line
        self.id = id

    def get_id(self):
        return self.id

    def get_type(self, tc):
        return tc.get_id_type(self.id)



