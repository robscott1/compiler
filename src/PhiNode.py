

class SSAStorageObject:

    def __init__(self, location, block):
        self.location = location
        self.block = block

    def to_text(self):
        return f"[{self.location}, {self.block.id}]"

    def to_value(self):
        if isinstance(self.location, PhiNode):
            return self.location.to_value()
        return self.location


class PhiNode:

    def __init__(self, block: str, var_target: str, type):
        self.block = block
        self.operands = []
        self.result = None
        self.var_target = var_target
        self.type = type

    """
    add_operand
    
    Adds a value read directly from read_value within SSAManager
    """
    def append_operand(self, op: str):
        self.operands.append(op)

    def set_result_register(self, reg: str):
        self.result = reg

    def to_text(self):
        operands = []
        for x, y in zip(self.operands, self.block.predecessors):
            operands.append(f"[{x}, {y.id}]")
        return f"{self.result} = phi {self.type.to_text()} {', '.join(operands)}"

    def to_value(self):
        return self.result
