import uuid

from ErrorOut import error_out
from ExtranceNode import ExtranceNode
from StatementIterator import StatementIterator
from Statements.AssignmentStatement import AssignmentStatement
from Statements.BlockStatement import BlockStatement
from Statements.ConditionalStatement import ConditionalStatement
from Statements.InvocationStatement import InvocationStatement
from Statements.PrintStatement import PrintStatement
from Statements.ReturnStatement import ReturnStatement
import graphviz

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
        self.id = str(uuid.uuid4())
        self.predecessors = []
        self.successors = []
        self.statements = []
        self.has_return = False
        self.visited = False
        self.label = label

    @classmethod
    def generate(cls, body, link_me, leaf_nodes):
        curr_node = ControlFlowNode()
        root = curr_node
        for node in link_me:
            curr_node.predecessors.append(node)
            node.successors.append(curr_node)
        link_me.clear()

        if isinstance(body, BlockStatement):
            body = body.statements

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
                    if len(then_node.successors) == 0:
                        link_me.add(then_node)
                    link_me.add(curr_node)
                else:
                    # Gotta add it again because it got cleared on the then_block
                    link_me.add(curr_node)
                    else_node = ControlFlowNode.generate(stmt.else_block, link_me, leaf_nodes)
                    if len(else_node.successors) == 0:
                        link_me.add(else_node)
                    if len(then_node.successors) == 0:
                        link_me.add(then_node)

                if body.has_next():
                    curr_node = cls.next_node(link_me)

            elif isinstance(stmt, WhileStatement):
                curr_node.statements.append(stmt)
                link_me.add(curr_node)
                then_do = ControlFlowNode.generate(stmt.body, link_me, leaf_nodes)
                if then_do.no_children():
                    link_me.add(then_do)
                converge = ControlFlowNode.generate([], link_me, leaf_nodes)
                converge.label = "while converge"
                converge.successors.append(curr_node)
                link_me.add(curr_node)

                if body.has_next():
                    curr_node = cls.next_node(link_me)

            else:
                curr_node.statements.append(stmt)

        return root

    def visualize_cfg(self, cfg, prev):
        if self.visited:
            cfg.edge(prev.id, self.id)
            return cfg
        self.visited = True
        if prev is not None:
            cfg.node(self.id, label=self.cfg_label())
            cfg.edge(prev.id, self.id)
        else:
            cfg.node(self.id, label=self.cfg_label())
        for node in self.successors:
            node.visualize_cfg(cfg, self)
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
            return "\n".join(list(map(lambda x: x.to_string(), self.statements)))
        else:
            return self.label






