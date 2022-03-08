
class InstructionsManager:

    def __init__(self, type_map):
        self._current_number = 0
        self.type_map = type_map
        self._values = self.set_values()
        self._ordered_instr_list = list()
        self._current_node = None

    def next_tmp(self):
        result = f"%t{self._current_number}"
        self._current_number += 1
        return result

    def set_values(self):
        values = {}
        values["READ_MEM"] = self.next_tmp()
        for _id in self.type_map.global_map.keys():
            values[_id] = f"@{_id}"
        return values


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

    def get_field_index(self, structure: str, field_id: str):
        return self.type_map.get_struct_field_idx(structure, field_id)

    def get_mem_size(self, structure: str):
        return self.type_map.get_mem_size(structure)



