from pytest import mark

from src.view import menu

value_params = {
    1,
    4,
    7,
    0,
    "a"
}

@mark.parametrize('expected_result', value_params)
def test_menu(expected_result):
    assert type(menu()) is int
