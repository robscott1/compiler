from ControlFlowNode import ControlFlowNode
from Factories.InstructionFactory import InstructionFactory
from Instructions.JumpInstruction import JumpInstruction
from InstructionsManager import InstructionsManager
from Statements.JumpStatement import JumpStatement
from Statements.WhileStatement import WhileStatement


class InstructionOrchestrator:

    def __init__(self, cfg, instr_mngr: InstructionsManager):
        self.cfg = cfg
        self.instr_mngr = instr_mngr

    def run(self, return_type, params, id):
        self.instruction_gen_traverse()
        text = self.generate_function_text(return_type, params, id)
        return text

    def generate_function_text(self, return_type, params, id):
        return_type = return_type.to_llvm_type()
        params = f"({', '.join(list(map(lambda x: x.to_llvm_type(), params)))})"
        ptr = "" if "%" not in return_type else "*"
        signature = f"define dso_local {return_type}{ptr} @{id}{params} {{"

        body = self.instruction_retrieval_traverse()
        body = "\n".join(body)

        result = [signature, body, "}\n"]
        return "\n".join(result)

    """
    instruction_retrieval_traverse
    
    Gets llvm text from every instruction in the control flow node.
    This is only the body, not the signature and brackets.
    """
    def instruction_retrieval_traverse(self):
        root: ControlFlowNode = self.cfg
        q = list()
        visited = set()
        q.append(root)

        instruction_list = []
        while q:
            node = q.pop(0)
            if not node.statements:
                continue
            visited.add(node.id)
            node.instructions = node.phi_nodes + node.instructions
            instruction_list.append(f"\n{node.id.split('%')[1]}:")
            instruction_text = node.get_llvm_text()
            instruction_list.append(instruction_text)


            for successor in node.successors:
                if successor.id not in visited:
                    visited.add(successor.id)
                    q.append(successor)

        return instruction_list

    def instruction_gen_traverse(self):
        root: ControlFlowNode = self.cfg
        q = list()
        visited = set()
        q.append(root)
        while q:
            node = q.pop(0)
            if not node.statements:
                continue
            # Might be revisiting unsealed nodes, only generate
            # instructions if it has not been sealed yet
            if node.id not in visited:
                self.generate_instructions(node)
            visited.add(node.id)
            q = self.add_valid_successors(node, visited, q)
            # Check to see if we can seal this node
            if self.is_sealable(node, visited):
                self.instr_mngr.ssa_seal_block(node)
                node.ssa_sealed = True
        return root


    """
    add_valid_successors
    
    Adds only nodes that are valid, under two conditions (OR)
        - the node has not been visited
        - the node is unsealed
    """
    def add_valid_successors(self, node, visited, q):
        predicate = lambda x: x.id not in visited or not x.ssa_sealed
        nxt = list(filter(predicate, node.successors))
        for successor in nxt:
            q.append(successor)
        return q
    """
    is_sealable
    
    Returns whether or not the node can be sealed. It checks two factors:
        - if there is 0 or 1 predecessors
        - if all of the predecessors have been visited
    If either of these are true, the node can be sealed.
    """
    def is_sealable(self, node, visited):
        if node.ssa_sealed:
            return False
        if len(node.predecessors) <= 1:
            return True
        else:
            for pred in node.predecessors:
                if pred.id not in visited:
                    return False
            return True

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


    def generate_instructions(self, node: ControlFlowNode):
        self.instr_mngr.clear_instructions_list()
        self.instr_mngr.set_current_node(node)
        for stmt in node.statements:
            InstructionFactory.create_instruction(stmt, self.instr_mngr)
        if (len(node.successors) == 1 and \
            not node.has_return and \
            not isinstance(node.statements[0], JumpStatement)
        ):
            successor = node.successors[0]
            self.instr_mngr.add_instruction(JumpInstruction("br label", successor.id))

        node.instructions = self.instr_mngr.get_complete_instructions()
