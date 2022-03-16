from queue import Queue

from ControlFlowNode import ControlFlowNode
from ErrorOut import error_out
from InstructionOrchestrator import InstructionOrchestrator
from InstructionsManager import InstructionsManager
from SSAManager import SSAManager
from Statements.WhileStatement import WhileStatement
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
        type_map.current_scope = self
        orchestrator = InstructionOrchestrator(self.cfg, instr_mngr)
        text = orchestrator.run(self.return_type, self.parameters, self.id)

        return text

    def gather_phi_nodes(self, ssa_mngr: SSAManager):
        print(ssa_mngr.current_def)

    def bfs_nodes(self, node: ControlFlowNode, instr_mngr):
        unsealed_nodes = []
        node_instr_list = []
        q = list()
        q.append(node)
        while len(q) != 0:
            curr = q.pop(0)
            if self.node_has_back_edge(curr):
                unsealed_nodes.append(curr)
            if curr.statements:
                instr_mngr.type_map.current_scope = self
                node_instr_list.append(f"\n{curr.id.split('%')[1]}:")
                # Generate the text, then operate on it to get phi nodes
                for successor in curr.successors:
                    if not successor.visited:
                        successor.visited = True
                        q.append(successor)
                    else:
                        self.back_edge_check(successor, unsealed_nodes, instr_mngr)

                curr.generate_llvm_text(instr_mngr)
                curr.instructions = curr.phi_nodes + curr.instructions
                node_instr = curr.get_llvm_text()
                node_instr_list.append(node_instr)

        return node_instr_list

    def back_edge_check(self, node, unsealed_nodes, instr_mngr):
        for unsealed in unsealed_nodes:
            if unsealed.id == node.id:
                instr_mngr.ssa_mngr.seal_block(node)
                node.ssa_sealed = True

    """
    node_has_back_edge
    
    Check to see if this node has a WhileStatement in its statements. 
    That is the only node that is potentially not sealed and is not 
    ready to read from predecessors.
    """
    def node_has_back_edge(self, node: ControlFlowNode):
        for stmt in node.statements:
            if isinstance(stmt, WhileStatement):
                return True
        return False

    def llvm_signature(self):
        type = self.return_type.to_llvm_type()
        params = f"({', '.join(list(map(lambda x: x.to_llvm_type(), self.parameters)))})"
        ptr = "" if "%" not in type else "*"
        return f"define dso_local {type}{ptr} @{self.id}{params} {{"
