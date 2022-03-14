from SSAStorageObject import SSAStorageObject


class PhiNode:

    def __init__(self, block: str, var_target: str):
        self.block = block
        self.operands = []
        self.result = None
        self.var_target = var_target

    """
    add_operand
    
    Adds a value read directly from read_value within SSAManager
    """
    def append_operand(self, op: str):
        self.operands.append(op)

    def set_result_register(self, reg: str):
        self.result = reg

    def to_text(self):
        operands = list(map(lambda x: x.to_value() if isinstance(x, SSAStorageObject) else x, self.operands))
        return f"{self.result} = phi({' '.join(operands)})"

    def to_value(self):
        return self.result


