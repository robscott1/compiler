from PhiNode import PhiNode


class SSAManager:

    def __init__(self):
        self.current_def = dict()
        self.sealed_blocks = set()
        # Under each key is a list of Phi's ?
        self.incomplete_phis = dict()

    """
    write_variable
    
    Writes variable value to respective variable WITHIN its CFG block
    """

    def write_variable(self, variable: str, block, value: str):
        if variable not in self.current_def:
            self.current_def[variable] = dict()
        self.current_def[variable][block.id] = value

    """
    read_variable
    
    Reads current value of variable within respective CFG block
    """
    def read_variable(self, variable: str, block):
        if block.id in self.current_def[variable]:
            return self.current_def[variable][block.id]
        else:
            return self.read_variable_from_predecessors(
                variable, block
            )

    """
    read_variable_from_predecessors
    
    Looks back through predecessors to find where this value can
    be assigned, either a new phi node or a value recently assigned
    that came from a sealed block.
    """
    def read_variable_from_predecessors(self, variable: str, block):
        if block.id not in self.sealed_blocks:
            value = PhiNode(block)
            if block.id not in self.incomplete_phis:
                self.incomplete_phis[block.id] = dict()
            self.incomplete_phis[block.id][variable] = value
        elif len(block.predecessors) == 0:
            value = None
        elif len(block.predecessors) == 1:
            value = self.read_variable(variable, block.predecessors[0])
        else:
            value = PhiNode(block)
            self.write_variable(variable, block, value)

        self.write_variable(variable, block, value)
        return value

    def add_phi_operands(self, variable: str, phi: PhiNode):
        for pred in phi.block.predecessors:
            phi.append_operator(self.read_variable(variable, pred))

    def seal_block(self, block):
        for variable in self.incomplete_phis[block.id].values():
            self.add_phi_operands(variable, self.incomplete_phis[block.id][variable])
        self.sealed_blocks[block.id] = block


