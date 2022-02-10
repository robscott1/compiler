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
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.predecessors = []
        self.successors = []
        self.statements = []
        self.has_return = False
        self.visited = False


    @classmethod
    def generate(cls, body, cfg, link_me):
        curr_node = ControlFlowNode()
        root = curr_node
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
            elif isinstance(stmt, ConditionalStatement):
                curr_node.statements.append(stmt)
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
                    curr_node = cls.next_node(cfg, link_me)

            elif isinstance(stmt, WhileStatement):
                curr_node.statements.append(stmt)
                link_me.add(curr_node)
                then_do, cfg = ControlFlowNode.generate(stmt.body, cfg, link_me)
                if then_do.no_children():
                    link_me.add(then_do)
                converge, cfg = ControlFlowNode.generate([], cfg, link_me)
                converge.successors.append(curr_node)
                cfg.edge(converge.id, curr_node.id)
                link_me.add(curr_node)

                if body.has_next():
                    curr_node = cls.next_node(cfg, link_me)

            else:
                curr_node.statements.append(stmt)

        return root, cfg

    def generate_cfg(self, cfg, prev):
        if self.visited:
            cfg.edge(prev.id, self.id)
            return cfg
        self.visited = True
        if prev is not None:
            cfg.node(self.id, label=self.instructions_string())
            cfg.edge(prev.id, self.id)
        else:
            cfg.node(self.id, label=self.instructions_string())
        for node in self.successors:
            node.generate_cfg(cfg, self)
        return cfg

    @classmethod
    def next_node(cls, cfg, link_me):
        tmp = ControlFlowNode()
        cfg.node(tmp.id)
        for node in link_me:
            tmp.predecessors.append(node)
            node.successors.append(tmp)
            cfg.edge(node.id, tmp.id)
        link_me.clear()
        return tmp

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

    def instructions_string(self):
        return "\n".join(list(map(lambda x: x.to_string(), self.statements)))






