from ErrorOut import error_out
from Statements.BlockStatement import BlockStatement
from Statements.ConditionalStatement import ConditionalStatement
from Statements.ReturnStatement import ReturnStatement


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
        self.child_nodes = []
        self.is_leaf = False

    @classmethod
    def generate(cls, body):
        node = ControlFlowNode()
        if isinstance(body, BlockStatement):
            body = body.statements
        for stmt in body:
            if isinstance(stmt, ReturnStatement):
                node.is_leaf = True
            if isinstance(stmt, ConditionalStatement):
                child_node = cls.generate(stmt.then_block)
                node.child_nodes.append(child_node)
                if stmt.else_block is not None:
                    child_node = cls.generate(stmt.else_block)
                    node.child_nodes.append(child_node)

        return node

    def valid_control_flow(self):
        return self.valid_path(self)

    def no_children(self):
        return len(self.child_nodes) == 0

    def valid_path(self, node):
        if node.no_children():
            return node.is_leaf
        for child in node.child_nodes:
            if not self.valid_path(child):
                return False
        return True





