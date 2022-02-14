class TemporaryMemoryManager:

    def __init__(self):
        self._current_number = 0
        self._values = dict()

    def next_tmp(self):
        result = f"%{self._current_number}"
        self._current_number += 1
        return result

    def get(self, id):
        return self._values.get(id)



