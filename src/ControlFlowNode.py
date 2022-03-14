import uuid
from random import random, randint

from Expressions.Expression import Expression
from Factories.InstructionFactory import InstructionFactory
from Instructions.JumpInstruction import JumpInstruction
from InstructionsManager import InstructionsManager
from StatementIterator import StatementIterator
from Statements.BlockStatement import BlockStatement
from Statements.ConditionalStatement import ConditionalStatement
from Statements.JumpStatement import JumpStatement
from Statements.ReturnStatement import ReturnStatement
from Statements.WhileStatement import WhileStatement


class ControlFlowNode:
    """
    ControlFlowNode

    Usage:
    Contains list of Statements. The Node is considered a leaf there is a
    ReturnStatement.

    If child_nodes is None AND is_leaf is False, then there the control
    flow of this function is illegal. This is true because the function will not
    return anything and it has gone as deep as possible on the function, given
    the control flow.

    @fields:
        - child_nodes (List<ControlFlowNode): links to traverse down the tree
        - is_leaf (Boolean): Identify whether the Node has a ReturnStatement
        - statements (List<Statement>): ?? idk if needed, list of statements

    """

    def __init__(self, label=None):
        self.id = f"%L{randint(1, 100)}"
        self.predecessors = []
        self.successors = []
        self.statements = []
        self.has_return = False
        self.visited = False
        self.label = label
        self.instructions = []
        self.phi_nodes = []

    @classmethod
    def generate(cls, body, link_me, leaf_nodes):
        curr_node = ControlFlowNode()
        root = curr_node
        for node in link_me:
            curr_node.predecessors.append(node)
            node.successors.append(curr_node)
        link_me.clear()

        if isinstance(body, Expression):
            curr_node.statements.append(body)
            return curr_node

        if isinstance(body, BlockStatement):
            body = body.statements

        body = cls.expand_block_stmts(body)

        body = StatementIterator(body)
        while body.has_next():
            stmt = body.next()
            if isinstance(stmt, ReturnStatement):
                curr_node.has_return = True
                curr_node.statements.append(stmt)
                leaf_nodes.add(curr_node)
                break
            elif isinstance(stmt, ConditionalStatement):
                curr_node.statements.append(stmt)
                link_me.add(curr_node)
                then_node = ControlFlowNode.generate(stmt.then_block, link_me, leaf_nodes)

                if stmt.else_block is None:
                    if len(then_node.successors) == 0 and not then_node.has_return:
                        link_me.add(then_node)
                    link_me.add(curr_node)
                else:
                    # Gotta add it again because it got cleared on the then_block
                    link_me.add(curr_node)
                    else_node = ControlFlowNode.generate(stmt.else_block, link_me, leaf_nodes)
                    if len(else_node.successors) == 0 and not else_node.has_return:
                        link_me.add(else_node)
                    if len(then_node.successors) == 0 and not then_node.has_return:
                        link_me.add(then_node)

                if body.has_next():
                    curr_node = cls.next_node(link_me)

            elif isinstance(stmt, WhileStatement):
                # Make new guard node and then build off that
                if len(curr_node.statements) != 0:
                    link_me.add(curr_node)
                    guard = ControlFlowNode()
                    guard.statements.append(stmt)
                    for node in link_me:
                        node.successors.append(guard)
                        guard.predecessors.append(node)
                    link_me.clear()
                    curr_node = guard
                else:
                    curr_node.statements.append(stmt)

                link_me.add(curr_node)
                then_do = ControlFlowNode.generate(stmt.body, link_me, leaf_nodes)
                if then_do.no_children():
                    link_me.add(then_do)
                jmp = JumpStatement(stmt.line, curr_node)
                converge = ControlFlowNode.generate([jmp], link_me, leaf_nodes)
                converge.successors.append(curr_node)
                link_me.add(curr_node)

                if body.has_next():
                    curr_node = cls.next_node(link_me)
                else:
                    leaf_nodes.add(curr_node)

            else:
                curr_node.statements.append(stmt)

        return root

    @classmethod
    def expand_block_stmts(cls, body: list):
        for stmt in body:
            if isinstance(stmt, BlockStatement):
                counter = 1
                for item in stmt.statements:
                    body.insert(body.index(stmt) + counter, item)
                    counter += 1
                body.remove(stmt)
        return body

    def visualize_cfg(self, cfg, prev, instr_mngr):
        if self.visited:
            cfg.edge(prev.id, self.id)
            return cfg
        self.visited = True
        if prev is not None:
            cfg.node(self.id, label=self.generate_instructions(instr_mngr))
            cfg.edge(prev.id, self.id)
        else:
            cfg.node(self.id, label=self.generate_instructions(instr_mngr))
        for node in self.successors:
            node.visualize_cfg(cfg, self, instr_mngr)
        return cfg

    @classmethod
    def next_node(cls, link_me):
        tmp = ControlFlowNode()
        for node in link_me:
            tmp.predecessors.append(node)
            node.successors.append(tmp)
        link_me.clear()
        return tmp

    def valid_control_flow(self):
        return self.valid_path(self)

    def no_children(self):
        return len(self.successors) == 0

    def valid_path(self, node):
        node.visited = True
        if node.no_children():
            return node.has_return
        for child in list(filter(lambda x: not x.visited, node.successors)):
            if not self.valid_path(child):
                return False
        return True

    def cfg_label(self):
        if self.label is None:
            return "\n".join(list(map(lambda x: x.to_string())))
        else:
            return self.label

    """
    Could we make text instructions in one pass so that it can do its thing in the
    event that there are more than one instructions involved?
    
    - create_instruction just returns string when its done, not as object instructions
    - but we want object instructions because we will be using that later to walk through
    """

    def generate_instructions(self, instr_mngr: InstructionsManager):
        instr_mngr.clear_instructions_list()
        instr_mngr.set_current_node(self)
        for stmt in self.statements:
            InstructionFactory.create_instruction(stmt, instr_mngr)
        if self.successors == 1 and not self.has_return:
            successor = self.successors[0]
            instr_mngr.add_instruction(JumpInstruction("br", successor.id))

        self.instructions = instr_mngr.get_complete_instructions()

        return "\n".join(list(map(lambda x: x.to_text(),
                                  self.instructions)))

    def generate_llvm_text(self, instr_mngr: InstructionsManager):
        instr_mngr.clear_instructions_list()
        instr_mngr.set_current_node(self)
        for stmt in self.statements:
            InstructionFactory.create_instruction(stmt, instr_mngr)
        if len(self.successors) == 1 and \
                not self.has_return \
                and not isinstance(self, JumpInstruction):
            successor = self.successors[0]
            instr_mngr.add_instruction(JumpInstruction("br label", successor.id))

        self.instructions = instr_mngr.get_complete_instructions()

    def get_llvm_text(self):
        return "\n".join(list(map(lambda x: x.to_text(),
                                  self.instructions)))