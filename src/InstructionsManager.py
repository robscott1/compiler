class InstructionsManager:

    def __init__(self, type_map):
        self._current_number = 0
        self._values = dict()
        self.type_map = type_map
        self._ordered_instr_list = list()
        self._current_node = None

    def next_tmp(self):
        result = f"%{self._current_number}"
        self._current_number += 1
        return result

    def get(self, id):
        return self._values.get(id)

    def store(self, id, tmp_location):
        self._values[id] = tmp_location

    def add_instruction(self, instr):
        self._ordered_instr_list.append(instr)

    def get_complete_instructions(self):
        return self._ordered_instr_list

    def has_value(self, id):
        return id in self._values

    def clear_instructions_list(self):
        self._ordered_instr_list.clear()

    def set_current_node(self, node):
        self._current_node = node

    def current_node(self):
        return self._current_node



