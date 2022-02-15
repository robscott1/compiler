import pytest

from Declaration import Declaration
from Factories.InstructionFactory import InstructionFactory
from InstructionsManager import InstructionsManager
from TypeChecker import TypeChecker
from conftest import program_to_json


@pytest.mark.parametrize(
    "file, code", [
        ("addition", Declaration("44", "int", "k")),
        ("addition", Declaration("44", "bool", "k"))
    ]
)
def test_allocation_instruction(file, code):
    params = program_to_json(f"../mini/{file}.mini")
    tc = TypeChecker(params)
    instr_mngr = InstructionsManager(tc)
    instr = InstructionFactory.create_instruction(code, instr_mngr)
    assert hasattr(instr, "result")
    assert hasattr(instr, "type")
    assert hasattr(instr, "op")


