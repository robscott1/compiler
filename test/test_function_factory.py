import pytest

from Function import Function
from Factories.FunctionFactory import FunctionFactory


@pytest.mark.parametrize(
    "input_dict, exp_dict", [
        ({'line': 17, 'id': 'f',
          'parameters': [],
          'return_type': 'A',
          'declarations': [], "body": []},
         {"size": 0})
    ]
)
def test_function_factory(input_dict, exp_dict):
    ff = FunctionFactory()
    func: Function = ff.generate(**input_dict)
    assert len(func.parameters) == exp_dict["size"]
