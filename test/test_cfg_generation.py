import graphviz
import pytest

from InstructionsManager import InstructionsManager
from TypeChecker import TypeChecker
from conftest import program_to_json


@pytest.mark.parametrize(
    "file", ["1",
             "dot",
             "ret-error",
             "while-loop",
             "while-with-if-hanging",
             "if-else-to-while",
             "ret",
             "addition",
             "dot-invocation",
             "dot-new",
             "read"
             ]
)
def test_cfg_generation(file):
    param = program_to_json(f"../mini/{file}.mini")
    tc = TypeChecker(param)
    main_fn = tc.fn_map.get("main")
    main_fn.create_cfg()
    test_cfg = main_fn.cfg.visualize_cfg(graphviz.Digraph(), None, InstructionsManager(tc))
    test_cfg.render(f"../cfg/gen/{file}")

