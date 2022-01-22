class Expression:

    '''
    This is to act as AbstractExpression because Python does not have
    interfaces.
    '''
    def __init__(self, line: int):
        self.line = line
