import pytest

from Declaration import Declaration
from TypeDeclaration import TypeDeclaration


@pytest.mark.parametrize(
    "type_dec, exp", [
        (TypeDeclaration
             (44, "x", [Declaration(44, "int", "i")]),
        "%struct.x = type { i32 }"),
        (TypeDeclaration
            (44, "B", [TypeDeclaration
                           (44, "X", [Declaration(44, "bool", "y")]),
                       Declaration(44, "int", "b")]),
         "%struct.B = type { %struct.X, i32 }")
    ]
)
def test_type_dec_to_text(type_dec, exp):
    assert type_dec.to_text() == exp

