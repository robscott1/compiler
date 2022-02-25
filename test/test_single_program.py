import graphviz

from InstructionsManager import InstructionsManager
from TypeChecker import TypeChecker
from conftest import program_to_json

PROGRAM = "if-else-to-while"

def test_single_program_cfg():
    file = PROGRAM
    param = program_to_json(f"../mini/{file}.mini")
    tc = TypeChecker(param)
    main_fn = tc.fn_map.get("main")
    main_fn.create_cfg()
    test_cfg = main_fn.cfg.visualize_cfg(graphviz.Digraph(), None, InstructionsManager(tc))
    test_cfg.render(f"../cfg/gen/{file}")