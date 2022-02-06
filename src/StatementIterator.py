class StatementIterator:

    def __init__(self, contents):
        self._length = len(contents)
        self._position = 0
        self._contents = contents

    def has_next(self):
        return self._position <= self._length - 1

    def next(self):
        item = self._contents[self._position]
        self._position += 1
        return item
