from ControlFlowNode import ControlFlowNode
from ErrorOut import error_out
from TemporaryMemoryManager import TemporaryMemoryManager
from Type import Type


class Function:

    def __init__(self, line: int, id: str, parameters: list,
                 return_type: Type, locals: list, body
                 ):
        self.line = line
        self.id = id
        self.parameters = parameters
        self.return_type = return_type
        self.locals = locals
        self.body = body
        self.cfg = None

    def id_in_scope(self, id: str):
        for decl in self.locals:
            if decl.id == id:
                return True
        return self.id_is_param(id)

    def get_id_type(self, id: str):
        for param in self.parameters:
            if param.id == id:
                return param.type
        for decl in self.locals:
            if decl.id == id:
                return decl.type
        return False

    def id_is_param(self, id: str):
        for param in self.parameters:
            if param.id == id:
                return True

    def analyze(self, tc):
        for stmt in self.body:
            stmt.analyze(tc)
        if not ControlFlowNode.generate(self.body, set(), set()).valid_control_flow():
            error_out(self.line, "Illegal control flow.", "611")

    def create_cfg(self):
        leaf_nodes = set()
        link_me = set()
        root = ControlFlowNode.generate(self.body, link_me, leaf_nodes)
        enter_node = ControlFlowNode()
        enter_node.statements = self.locals
        enter_node.successors.append(root)
        exit_node = ControlFlowNode(label="Exit")
        for leaf in leaf_nodes:
            leaf.successors.append(exit_node)
            exit_node.predecessors.append(leaf)
        self.cfg = enter_node

    def generate_llvm(self, type_map, local_map):
        mem_mngr = TemporaryMemoryManager()
        self.cfg.generate_instructions(type_map, local_map, mem_mngr)










