# This test is based on the example from ret.mini
import graphviz
import pytest as pytest

from ControlFlowNode import ControlFlowNode
from InstructionsManager import InstructionsManager
from Statements.BlockStatement import BlockStatement
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
        ("while-if-else-no-end-ret", True),
    ]
)
def test_valid_control_flow(input_file, exp_outcome):
    params = program_to_json(f"../mini/{input_file}.mini")
    tc = TypeChecker(params)
    for fn in tc.fn_map.values():
        root = ControlFlowNode.generate(fn.body, set(), set())
        assert root.valid_control_flow() == exp_outcome

@pytest.mark.parametrize(
    "input_file", [
        "addition",
    ]
)
def test_enter_node_instructions(input_file):
    params = program_to_json(f"../mini/{input_file}.mini")
    tc = TypeChecker(params)
    main_fn = tc.fn_map.get("main")
    instr_mngr = InstructionsManager(tc)
    main_fn.create_cfg()
    cfg = main_fn.cfg.visualize_cfg(graphviz.Digraph(), None, instr_mngr)
    cfg.render(f"../cfg/{input_file}")

@pytest.mark.parametrize(
    "body, expected", [
        ([1, 2, BlockStatement(-1, [3, 4])], [1, 2, 3, 4]),
        ([BlockStatement(-1, [1, 2]), 3, 4], [1, 2, 3, 4]),
        ([1, BlockStatement(-1, [2, 3]), 4], [1, 2, 3, 4]),
        ([1,2,3,4], [1,2,3,4])
    ]
)
def test_expand_block_stmts(body, expected):
    result = ControlFlowNode.expand_block_stmts(body)
    assert result == expected