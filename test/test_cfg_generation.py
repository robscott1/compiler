import graphviz
import pytest

from ControlFlowNode import ControlFlowNode
from TypeChecker import TypeChecker
from conftest import program_to_json


@pytest.mark.parametrize(
    "file", ["simple-if-else-no-end-return",
             "ret-error",
             "while-loop",
             "while-with-if-hanging",
             "while-if-else-no-end-ret"]
)
def test_cfg_generation(file):
    param = program_to_json(f"../mini/{file}.mini")
    tc = TypeChecker(param)
    main_fn = tc.fn_map.get("main")
    graph, cfg = ControlFlowNode.generate(main_fn.body, graphviz.Digraph(), set())
    cfg.render(f"../cfg/{file}")
