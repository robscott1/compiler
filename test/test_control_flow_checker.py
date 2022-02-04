# This test is based on the example from ret.mini
from ControlFlowNode import ControlFlowNode
from TypeChecker import TypeChecker
from conftest import program_to_json


def test_build_control_flow_check():
    cfn_list = []
    params = program_to_json("../mini/ret.mini")
    tc = TypeChecker(params)
    for fn in tc.fn_map.values():
        root = ControlFlowNode.generate(fn.body)
        cfn_list.append(root)
    assert len(cfn_list) == 2


def test_valid_control_flow():
    params = program_to_json("../mini/ret.mini")
    tc = TypeChecker(params)
    for fn in tc.fn_map.values():
        root = ControlFlowNode.generate(fn.body)
        assert root.valid_control_flow()
