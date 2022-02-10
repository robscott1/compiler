# This test is based on the example from ret.mini
import graphviz
import pytest as pytest

from ControlFlowNode import ControlFlowNode
from TypeChecker import TypeChecker
from conftest import program_to_json


@pytest.mark.parametrize(
    "input_file, exp_outcome", [
        ("ret", True),
        ("ret-error", False),
        ("simple-if-else-no-end-return", False),
        ("while-loop", True),
        ("while-with-if-hanging", True),
        ("if-else-to-while", True),
        ("while-if-else-no-end-ret", True)
    ]
)
def test_valid_control_flow(input_file, exp_outcome):
    params = program_to_json(f"../mini/{input_file}.mini")
    tc = TypeChecker(params)
    for fn in tc.fn_map.values():
        root, cfg = ControlFlowNode.generate(fn.body, graphviz.Digraph(), set())
        assert root.valid_control_flow() == exp_outcome
