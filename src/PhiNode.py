class PhiNode:

    def __init__(self, block: str):
        self.block = block
        self.operands = []
        self.result = None

    """
    add_operand
    
    Adds a value read directly from read_value within SSAManager
    """
    def add_operand(self, op: str):
        self.operands.append(op)

    def set_result_register(self, reg: str):
        self.result = reg

    def to_text(self):
        return f"{self.result} = phi({', '.join(self.operands)})"


