# This test is based on the example from ret.mini
from ControlFlowNode import ControlFlowNode


def test_build_control_flow_check(control_flow_example):
    cfn_list = []
    for fn in control_flow_example.fn_map.values():
        root = ControlFlowNode.generate(fn.body)
        cfn_list.append(root)
    assert len(cfn_list) == 2


def test_valid_control_flow(control_flow_example):
    for fn in control_flow_example.fn_map.values():
        root = ControlFlowNode.generate(fn.body)
        assert root.valid_control_flow()
