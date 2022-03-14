from ControlFlowNode import ControlFlowNode
from ErrorOut import error_out
from InstructionsManager import InstructionsManager
from SSAManager import SSAManager
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
        enter_node.statements = self.locals + self.parameters
        enter_node.successors.append(root)
        exit_node = ControlFlowNode(label="Exit")
        for leaf in leaf_nodes:
            leaf.successors.append(exit_node)
            exit_node.predecessors.append(leaf)
        self.cfg = enter_node

    def generate_llvm(self, type_map):
        instr_mngr = InstructionsManager(type_map)
        self.cfg.generate_instructions(instr_mngr)

    def llvm_representation(self, type_map):
        instr_mngr = InstructionsManager(type_map)
        lines = []

        # recreate CFG so that the nodes arent marked as visited
        self.create_cfg()

        lines.append(self.llvm_signature())
        body = self.bfs_nodes(self.cfg, [], instr_mngr)
        lines.append("\n".join(body))
        lines.append("}\n")
        return "\n".join(lines)

    def gather_phi_nodes(self, ssa_mngr: SSAManager):
        print(ssa_mngr.current_def)

    def bfs_nodes(self, node: ControlFlowNode, node_instr_list, instr_mngr):
        node.visited = True
        if node.statements:
            instr_mngr.type_map.current_scope = self
            node_instr_list.append(f"\n{node.id.split('%')[1]}:")
            node.generate_llvm_text(instr_mngr)
            # Generate the text, then operate on it to get phi nodes
            node_instr = node.get_llvm_text()
            node_instr_list.append(node_instr)
        for successor in node.successors:
            if not successor.visited:
                node_instr_list = self.bfs_nodes(successor, node_instr_list, instr_mngr)
        self.gather_phi_nodes(instr_mngr.ssa_mngr)
        return node_instr_list

    def llvm_signature(self):
        type = self.return_type.to_llvm_type()
        params = f"({', '.join(list(map(lambda x: x.to_llvm_type(), self.parameters)))})"
        ptr = "" if "%" not in type else "*"
        return f"define dso_local {type}{ptr} @{self.id}{params} {{"
