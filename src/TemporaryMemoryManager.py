class TemporaryMemoryManager:

    def __init__(self):
        self._current_number = 0

    def next_tmp(self):
        result = f"%{self._current_number}"
        self._current_number += 1
        return result
