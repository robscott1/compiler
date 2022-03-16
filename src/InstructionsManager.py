from copy import deepcopy

from PhiNode import PhiNode
from SSAManager import SSAManager


class InstructionsManager:

    def __init__(self, type_map):
        self._current_number = 0
        self.type_map = type_map
        self._values = self.set_values()
        self._ordered_instr_list = list()
        self._current_node = None
        self.ssa_mngr = SSAManager()

    def next_tmp(self, __id=None):
        if __id is not None:
            result = f"%{__id}"
        else:
            result = f"%t{self._current_number}"
            self._current_number += 1
        return result

    """
    @returns: location, from_phi
        - location: where the value is stored currently, or constant val
        - load_result: If the result was written within its own block or
            came from a phi node, this value is False. Otherwise True
    """
    def ssa_read_variable(self, location: str, type):
        result = self.ssa_mngr.read_variable(location, self._current_node, type)

        if isinstance(result, PhiNode):
            phi_register_location = self.next_tmp()
            result.set_result_register(phi_register_location)
            self._current_node.phi_nodes.append(result)
            return phi_register_location
        return result

    def ssa_seal_block(self, node):
        self.ssa_mngr.seal_block(node)

    def set_values(self):
        values = {}
        values["@READ_MEM"] = f"@READ_MEM"
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
        new_list = deepcopy(self._ordered_instr_list)
        return new_list

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

    def get_field_type(self, structure: str, field_id: str):
        return self.type_map.get_struct_field_type(structure, field_id)

    def get_mem_size(self, structure: str):
        return self.type_map.get_mem_size(structure)



