import subprocess

import graphviz
import pytest

from InstructionsManager import InstructionsManager
from TypeChecker import TypeChecker
from conftest import program_to_json

PROGRAM = "simple-if-else"
@pytest.mark.skip("only for debugging purposes, not for test suite")
def test_single_program_cfg():
    file = PROGRAM
    param = program_to_json(f"{file}")
    tc = TypeChecker(param)
    main_fn = tc.fn_map.get("main")
    main_fn.create_cfg()
    test_cfg = main_fn.cfg.visualize_cfg(graphviz.Digraph(), None, InstructionsManager(tc))
    test_cfg.render(f"../cfg/{file}")