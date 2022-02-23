from InstructionsManager import InstructionsManager


def test_get_mem_size(type_checker):
    instr_mngr = InstructionsManager(type_checker)
    assert instr_mngr.get_mem_size("A") == '4'