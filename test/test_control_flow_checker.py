# This test is based on the example from ret.mini
import graphviz
import pytest as pytest

from ControlFlowNode import ControlFlowNode
from TypeChecker import TypeChecker
from conftest import program_to_json

@pytest.mark.skip("in progress")
def test_build_control_flow_check():
    cfn_list = []
    params = program_to_json("../mini/simple-if-else")
    tc = TypeChecker(params)
    for fn in tc.fn_map.values():
        root = ControlFlowNode.generate(fn.body)
        cfn_list.append(root)
    assert len(cfn_list) == 2


def test_valid_control_flow():
    params = program_to_json("../mini/ret.mini")
    tc = TypeChecker(params)
    for fn in tc.fn_map.values():
        root, cfg = ControlFlowNode.generate(fn.body, graphviz.Digraph(), set())
        assert root.valid_control_flow()
