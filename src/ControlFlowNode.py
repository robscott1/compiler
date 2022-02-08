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
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.predecessors = []
        self.successors = []
        self.statements = []
        self.has_return = False

    @classmethod
    def generate(cls, body, cfg, link_me):
        curr_node = ControlFlowNode()
        cfg.node(curr_node.id)
        for node in link_me:
            curr_node.predecessors.append(node)
            node.successors.append(curr_node)
            cfg.edge(node.id, curr_node.id)
        link_me.clear()

        if isinstance(body, BlockStatement):
            body = body.statements

        body = StatementIterator(body)
        while body.has_next():
            stmt = body.next()
            if isinstance(stmt, ReturnStatement):
                curr_node.has_return = True
                curr_node.statements.append(stmt)
                break
            if isinstance(stmt, PrintStatement):
                curr_node.statements.append(stmt)
            if isinstance(stmt, AssignmentStatement):
                curr_node.statements.append(stmt)
            if isinstance(stmt, InvocationStatement):
                curr_node.statements.append(stmt)
            if isinstance(stmt, ConditionalStatement):
                link_me.add(curr_node)
                then_node, cfg = ControlFlowNode.generate(stmt.then_block, cfg, link_me)
                if stmt.else_block is None:
                    if len(then_node.successors) == 0:
                        link_me.add(then_node)
                    link_me.add(curr_node)
                else:
                    # Gotta add it again because it got cleared on the then_block
                    link_me.add(curr_node)
                    else_node, cfg = ControlFlowNode.generate(stmt.else_block, cfg, link_me)
                    if len(else_node.successors) == 0:
                        link_me.add(else_node)
                    if len(then_node.successors) == 0:
                        link_me.add(then_node)

                if body.has_next():
                    tmp = ControlFlowNode()
                    cfg.node(tmp.id)
                    for node in link_me:
                        tmp.predecessors.append(node)
                        node.successors.append(tmp)
                        cfg.edge(node.id, tmp.id)
                    link_me.clear()
                    curr_node = tmp

        return curr_node, cfg

    def valid_control_flow(self):
        return self.valid_path(self)

    def no_children(self):
        return len(self.successors) == 0

    def valid_path(self, node):
        if node.no_children():
            return node.has_return
        for child in node.successors:
            if not self.valid_path(child):
                return False
        return True





