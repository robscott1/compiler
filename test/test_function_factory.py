import pytest

from Function import Function
from FunctionFactory import FunctionFactory


@pytest.mark.parametrize(
    "input_dict, exp_dict", [
        ({'line': 17, 'id': 'f',
          'parameters': [{'line': 17, 'type': 'int', 'id': 'i'}, {'line': 17, 'type': 'B', 'id': 'j'}],
          'return_type': 'A',
          'locals': [{'line': 19, 'type': 'int', 'id': 'f'}, {'line': 19, 'type': 'int', 'id': 'l'},
                           {'line': 19, 'type': 'int', 'id': 'k'}], 'body': [{'line': 20, 'stmt': 'return',
                                                                              'exp': {'line': 20, 'exp': 'dot',
                                                                                      'left': {'line': 20, 'exp': 'dot',
                                                                                               'left': {'line': 20,
                                                                                                        'exp': 'dot',
                                                                                                        'left': {
                                                                                                            'line': 20,
                                                                                                            'exp': 'dot',
                                                                                                            'left': {
                                                                                                                'line': 20,
                                                                                                                'exp': 'id',
                                                                                                                'id': 'b'},
                                                                                                            'id': 'a'},
                                                                                                        'id': 'a'},
                                                                                               'id': 'a'},
                                                                                      'id': 'a'}}]},
         {"size": 2})

    ]
)
def test_function_factory(input_dict, exp_dict):
    ff = FunctionFactory()
    print(input_dict)
    func: Function = ff.generate(**input_dict)
    assert len(func.parameters) == exp_dict["size"]
