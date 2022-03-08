import pytest

from Declaration import Declaration


@pytest.mark.parametrize(
    "glb, exp", [
        (Declaration(44, "int", "x"),
         "@x = common dso_local global i32 0"),
        (Declaration(44, "A", "x"),
         "@x = common dso_local global %tstruct.A 0")
    ]
)
def test_global_declaration(glb, exp):
    assert glb.to_global_declaration() == exp
