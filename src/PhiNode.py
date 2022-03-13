class PhiNode:

    def __init__(self, block: str):
        self.block = block
        self.operands = []

    """
    add_operand
    
    Adds a value read directly from read_value within SSAManager
    """
    def add_operand(self, op: str):
        self.operands.append(op)

