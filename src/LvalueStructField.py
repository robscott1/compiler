from LvalueId import LvalueId


class LvalueStructField(LvalueId):

    def __init__(self, line: int, left: dict, id: str):
        super(LvalueStructField, self,).__init__(line, id)
        self.left = left.get("id")

    def get_id(self):
        return self.left

    def get_type(self, tc):
        structure = tc.get_id_type(self.left)
        return tc.get_struct_field_type(structure, self.id)
